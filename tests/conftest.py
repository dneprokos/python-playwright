import pytest
from pathlib import Path
from dotenv import load_dotenv
from config.config import Config

# Load .env file so os.getenv() calls in Config pick up local overrides.
# override=False means shell-exported vars take priority over .env values.
load_dotenv(override=False)


# Extends pytest CLI with custom arguments. Defaults come from Config (which
# reads .env), so you can override at runtime: pytest --headless=False
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default=Config.BROWSER)
    parser.addoption("--headless", action="store", default=str(Config.HEADLESS))
    parser.addoption("--full_screenshot", action="store", default="False")


# pytest-playwright picks up this fixture name automatically to configure
# how the browser process is launched (not the context/tab).
@pytest.fixture(scope="session")
def browser_type_launch_args(pytestconfig):
    return {
        "headless": pytestconfig.getoption("--headless").lower() == "true",
        "args": ["--start-maximized"]
    }


# pytest-playwright picks up this fixture name automatically to configure
# the browser context (viewport, HTTPS errors, cookies, etc.).
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True
    }


# pytest-playwright uses this fixture name to override the base URL for
# page.goto("/path") calls — no need to hardcode full URLs in tests.
@pytest.fixture(scope="session")
def base_url():
    return Config.BASE_URL


# autouse=True means this runs before every test without being requested.
# Ensures output directories exist so screenshot/data writes never fail.
@pytest.fixture(autouse=True)
def setup_test_environment():
    Config.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    Config.TEST_DATA_DIR.mkdir(parents=True, exist_ok=True)
    yield


# Overrides pytest-playwright's default page fixture to apply global timeouts.
# scope="function" (default) means a fresh page per test.
@pytest.fixture(scope="function")
def page(page):
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    return page


# hookwrapper=True lets us intercept the result after pytest builds the report.
# We use it to capture a screenshot whenever a test call phase fails,
# so CI failures are always paired with visual evidence.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    # Attach phase result to item so other fixtures can read it (e.g. rep_call).
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed and Config.SCREENSHOT_ON_FAILURE:
        try:
            # Try plain page fixture first; fall back to last page in context.
            page = item.funcargs.get("page") or (
                item.funcargs.get("context").pages[-1]
                if item.funcargs.get("context")
                else None
            )
            if page:
                full = eval(item.config.getoption("--full_screenshot"))
                path = Config.SCREENSHOTS_DIR / f"{item.name}.png"
                page.screenshot(path=str(path), full_page=full)
        except Exception as e:
            print(f"Screenshot failed: {e}")

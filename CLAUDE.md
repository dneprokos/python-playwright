# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests (PYTHONPATH must include project root)
PYTHONPATH=$(pwd) pytest

# Run single test file
PYTHONPATH=$(pwd) pytest tests/test_home_page.py

# Run single test by name
PYTHONPATH=$(pwd) pytest tests/test_home_page.py::TestClassName::test_method_name

# Run by marker
PYTHONPATH=$(pwd) pytest -m smoke
PYTHONPATH=$(pwd) pytest -m regression

# Run headed (visible browser)
PYTHONPATH=$(pwd) pytest --headless=False

# Run in different browser
PYTHONPATH=$(pwd) pytest --browser firefox

# Run in parallel
PYTHONPATH=$(pwd) pytest -n auto

# Generate HTML report
PYTHONPATH=$(pwd) pytest --html=test-results/report.html
```

On Windows set PYTHONPATH via: `$env:PYTHONPATH = (Get-Location).Path`

## Architecture

Two-layer inheritance chain governs all tests:

```
BasePage  ←  specific Page (e.g. HomePage, BasicAuthPage)
BaseTest  ←  specific Test class (e.g. TestHomePage)
```

**`framework/page_base/base_page.py`** — `BasePage` wraps `playwright.Page`. All page objects inherit it. Provides `navigate(path)`, `click`, `fill`, `get_text`, `wait_for_load_state`, `take_screenshot`. Use `self.page` for raw Playwright access when base methods are insufficient.

**`framework/test_base/base_test.py`** — `BaseTest` is a pytest class. Its `autouse` fixture injects `self.page` and `self.base_url`, then navigates to `base_url` before each test. All test classes inherit `BaseTest` instead of using plain pytest functions.

**`pages/`** — one file per page of the app under test. Each class inherits `BasePage`, holds locators and page-specific actions. No assertions here.

**`tests/`** — one file per page. Test classes inherit `BaseTest`. Assertions live here.

**`tests/conftest.py`** — pytest-playwright fixture overrides (`browser_type_launch_args`, `browser_context_args`, `base_url`, `page`) plus screenshot-on-failure hook. `.env` is loaded here via `python-dotenv`.

**`config/config.py`** — single `Config` class, all settings as class attributes. Reads env vars; `.env` file supported. `BROWSER`, `HEADLESS`, `BASE_URL`, timeouts, paths.

## Key conventions

- Tests run against `https://the-internet.herokuapp.com` (set in `Config.BASE_URL`)
- `PYTHONPATH` must include repo root — imports are absolute from root (e.g. `from pages.home_page import HomePage`)
- CI runs only Chromium (see `.github/workflows/test.yml`)
- Custom CLI args (`--headless`, `--browser_name`, `--full_screenshot`) defined in `conftest.py::pytest_addoption` — these override `.env`/`Config` at runtime
- Screenshots on failure auto-save to `test-results/screenshots/<test_name>.png` when `Config.SCREENSHOT_ON_FAILURE = True`
- `BasePage.get_title()` is async — don't call it from sync tests; use `page.title()` directly instead

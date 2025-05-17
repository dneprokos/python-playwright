import os
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from config.config import Config

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure browser launch arguments."""
    return {
        "headless": Config.HEADLESS,
        "args": ["--start-maximized"]
    }

@pytest.fixture(scope="session")
def browser_context_args():
    """Configure browser context arguments."""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True
    }

@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for the application."""
    return Config.BASE_URL

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment before each test."""
    # Create necessary directories
    Config.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    Config.TEST_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    yield
    
    # Cleanup after test if needed
    pass

@pytest.fixture(scope="function")
def page(page):
    """Configure page with default timeout and other settings."""
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    return page 
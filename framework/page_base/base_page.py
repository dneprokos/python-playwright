from playwright.sync_api import Page, expect
from config.config import Config
import logging
from pathlib import Path


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate(self, path: str = ""):
        """Navigate to a specific path on the base URL."""
        url = f"{Config.BASE_URL}{path}"
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def wait_for_selector(self, selector: str, timeout: int = None):
        """Wait for an element to be visible."""
        timeout = timeout or Config.DEFAULT_TIMEOUT
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str):
        """Click an element with logging."""
        self.logger.info(f"Clicking element: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        """Fill an input field with logging."""
        self.logger.info(f"Filling field {selector} with value: {value}")
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        """Get text content of an element."""
        return self.page.locator(selector).inner_text()

    def take_screenshot(self, name: str):
        """Take a screenshot and save it to the configured directory."""
        if Config.SCREENSHOT_ON_FAILURE:
            screenshot_path = Config.SCREENSHOTS_DIR / f"{name}.png"
            self.page.screenshot(path=str(screenshot_path))
            self.logger.info(f"Screenshot saved to: {screenshot_path}")

    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        return self.page.locator(selector).is_visible()

    def wait_for_load_state(self, state: str = "networkidle"):
        """Wait for the page to reach a specific load state."""
        self.page.wait_for_load_state(state)

    async def get_title(self):
        return await self.page.title()

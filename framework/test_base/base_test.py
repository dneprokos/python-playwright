import pytest
from playwright.sync_api import Page
from framework.page_base.base_page import BasePage


class BaseTest:
    """Base test class that provides common setup and teardown functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, base_url: str):
        """Setup for each test.
        
        Args:
            page: Playwright page object
            base_url: Base URL of the application
        """
        self.page = page
        self.base_url = base_url
        self.page.goto(self.base_url)
        
    def take_screenshot(self, name: str):
        """Take a screenshot of the current page.
        
        Args:
            name: Name of the screenshot file
        """
        self.page.screenshot(path=f"test-results/screenshots/{name}.png")
        
    def get_page_title(self) -> str:
        """Get the current page title.
        
        Returns:
            str: The page title
        """
        return self.page.title()
        
    def wait_for_page_load(self):
        """Wait for the page to be fully loaded."""
        self.page.wait_for_load_state("networkidle") 
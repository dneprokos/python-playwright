import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from framework.test_base.base_test import BaseTest


class TestHomePage(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_home_page(self):
        """Setup specific to home page tests."""
        self.home_page = HomePage(self.page)
        self.wait_for_page_load()

    def test_verify_available_content(self):
        """Test to verify all menu items are present and correct."""
        # Arrange
        expected_menu_items = [
            ('/abtest', 'A/B Testing'),
            ('/add_remove_elements/', 'Add/Remove Elements'),
            ('/basic_auth', 'Basic Auth'),
            ('/broken_images', 'Broken Images'),
            ('/challenging_dom', 'Challenging DOM'),
            ('/checkboxes', 'Checkboxes'),
            ('/context_menu', 'Context Menu'),
            ('/digest_auth', 'Digest Authentication'),
            ('/disappearing_elements', 'Disappearing Elements'),
            ('/drag_and_drop', 'Drag and Drop'),
            ('/dropdown', 'Dropdown'),
            ('/dynamic_content', 'Dynamic Content'),
            ('/dynamic_controls', 'Dynamic Controls'),
            ('/dynamic_loading', 'Dynamic Loading'),
            ('/entry_ad', 'Entry Ad'),
            ('/exit_intent', 'Exit Intent'),
            ('/download', 'File Download'),
            ('/upload', 'File Upload'),
            ('/floating_menu', 'Floating Menu'),
            ('/forgot_password', 'Forgot Password'),
            ('/login', 'Form Authentication'),
            ('/frames', 'Frames'),
            ('/geolocation', 'Geolocation'),
            ('/horizontal_slider', 'Horizontal Slider'),
            ('/hovers', 'Hovers'),
            ('/infinite_scroll', 'Infinite Scroll'),
            ('/inputs', 'Inputs'),
            ('/jqueryui/menu', 'JQuery UI Menus'),
            ('/javascript_alerts', 'JavaScript Alerts'),
            ('/javascript_error', 'JavaScript onload event error'),
            ('/key_presses', 'Key Presses'),
            ('/large', 'Large & Deep DOM'),
            ('/windows', 'Multiple Windows'),
            ('/nested_frames', 'Nested Frames'),
            ('/notification_message', 'Notification Messages'),
            ('/redirector', 'Redirect Link'),
            ('/download_secure', 'Secure File Download'),
            ('/shadowdom', 'Shadow DOM'),
            ('/shifting_content', 'Shifting Content'),
            ('/slow', 'Slow Resources'),
            ('/tables', 'Sortable Data Tables'),
            ('/status_codes', 'Status Codes'),
            ('/typos', 'Typos'),
            ('/tinymce', 'WYSIWYG Editor'),
        ]

        # Act
        menu_items = self.home_page.get_menu_items_href_and_text()

        # Assert
        expect(self.page.locator("h1")).to_contain_text(
            "Welcome to the-internet")
        expect(self.page.locator("h2")).to_contain_text("Available Examples")
        assert menu_items == expected_menu_items, f"Menu items do not match.\nExpected: {expected_menu_items}\nActual: {menu_items}"

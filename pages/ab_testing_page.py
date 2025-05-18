from playwright.sync_api import Page
from framework.page_base.base_page import BasePage


class AbTestingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_header_locator = self.page.locator('h3')
        self.contentText = self.page.locator('div.example >p')

    def get_page_header(self):
        return self.page_header_locator.text_content()

    def get_context_text(self):
        return self.contentText.text_content().strip()

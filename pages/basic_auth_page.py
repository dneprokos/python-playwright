from framework.page_base.base_page import BasePage
from playwright.sync_api import Page


class BasicAuthPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_header = self.page.locator('h3')

    def get_page_header(self):
        return self.page_header.inner_text().strip()

    def get_paragraph_text(self):
        return self.page.text_content('.example p').strip()

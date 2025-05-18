from playwright.sync_api import Page, Locator
from framework.page_base.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_header: Locator = self.page.locator("h3")
        self.addElementButton: Locator = self.page.get_by_role(
            'button', name='Add Element')

    def get_page_header(self):
        self.page_header.wait_for(state="visible", timeout=5000)
        return self.page_header.inner_text().strip()

    def get_all_delete_buttons(self):
        return self.page.get_by_role('button', name='Delete').all()

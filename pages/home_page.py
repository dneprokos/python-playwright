from framework.page_base.base_page import BasePage
from playwright.sync_api import Page


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def get_menu_items_href_and_text(self):
        link_elements = self.page.locator("ul li a")
        count = link_elements.count()
        menu_items = []

        for i in range(count):
            href = link_elements.nth(i).get_attribute("href")
            text = link_elements.nth(i).inner_text()
            menu_items.append((href, text.strip()))

        return menu_items
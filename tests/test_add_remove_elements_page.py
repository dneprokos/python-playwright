from typing import List
import pytest
from framework.test_base.base_test import BaseTest
from pages.add_remove_elements_page import AddRemoveElementsPage
from playwright.sync_api import Locator, expect


class TestAddRemoveElements(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_add_remove_elements_page(self):
        """Setup specific to Add Remove Elements page tests."""
        self.page.goto(f"{self.base_url}/add_remove_elements/")
        self.wait_for_page_load()
        self.add_remove_elements_page = AddRemoveElementsPage(self.page)

    def test_verify_page_content(self):
        # Act
        page_header: str = self.add_remove_elements_page.get_page_header()
        add_element_btn: Locator = self.add_remove_elements_page.addElementButton
        delete_btns: List[Locator] = self.add_remove_elements_page.get_all_delete_buttons(
        )

        # Assert
        assert page_header == 'Add/Remove Elements'
        expect(add_element_btn).to_be_enabled()
        assert len(delete_btns) == 0

    def test_add_element_should_be_added(self):
        # Act
        self.add_remove_elements_page.addElementButton.click()
        delete_btns: List[Locator] = self.add_remove_elements_page.get_all_delete_buttons(
        )

        # Assert
        assert len(delete_btns) == 1

    def test_add_multiple_elements_should_be_added(self):
        # Arrange
        add_actions_number = 3

        # Act
        for _ in range(add_actions_number):
            self.add_remove_elements_page.addElementButton.click()
        delete_btns: List[Locator] = self.add_remove_elements_page.get_all_delete_buttons(
        )

        # Assert
        assert len(delete_btns) == 3

    def test_click_delete_button_should_be_deleted(self):
        # Arrange
        self.add_remove_elements_page.addElementButton.click()
        delete_btns: List[Locator] = self.add_remove_elements_page.get_all_delete_buttons(
        )

        # Act
        delete_btns[0].click()
        delete_btns = self.add_remove_elements_page.get_all_delete_buttons()

        # Assert
        assert len(delete_btns) == 0

    def test_delete_multiple_elements_should_be_deleted(self):
        # Arrange
        add_actions_number = 3
        for _ in range(add_actions_number):
            self.add_remove_elements_page.addElementButton.click()

        # Act
        delete_btns = self.add_remove_elements_page.get_all_delete_buttons()
        delete_btns[0].click()
        delete_btns[1].click()
        delete_btns = self.add_remove_elements_page.get_all_delete_buttons()

        # Assert
        assert len(delete_btns) == 1

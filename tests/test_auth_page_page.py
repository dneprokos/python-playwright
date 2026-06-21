import pytest
from framework.test_base.base_test import BaseTest
from pages.basic_auth_page import BasicAuthPage


class TestBasicAuth(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_add_remove_elements_page(self):
        """Setup specific to Add Remove Elements page tests."""
        self.basic_auth_url = f"{self.base_url.replace('https://', '')}"  # strip schema if needed
        self.page.goto(
            f"https://admin:admin@{self.basic_auth_url}/basic_auth/")
        self.wait_for_page_load()
        self.basic_auth_page = BasicAuthPage(self.page)

    def test_verify_successfull_authorization(self):
        assert self.basic_auth_page.get_page_header() == "Basic Auth"
        assert self.basic_auth_page.get_paragraph_text() == "Congratulations! You must have the proper credentials."

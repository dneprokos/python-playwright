import pytest
from framework.test_base.base_test import BaseTest
from pages.ab_testing_page import AbTestingPage


class TestAbTestingPage(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_ab_testing_page(self):
        """Setup specific to AB Testing page tests."""
        self.page.goto(f"{self.base_url}/abtest")
        self.wait_for_page_load()
        self.ab_testing_page = AbTestingPage(self.page)

    def test_verify_available_content(self):
        # Arrange
        expected_page_headers = ['A/B Test Variation 1', 'A/B Test Control']
        expected_page_text = 'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through).'

        # Act
        page_header: str = self.ab_testing_page.get_page_header()
        context_text: str = self.ab_testing_page.get_context_text()

        # Assert
        assert page_header in expected_page_headers
        assert expected_page_text in context_text

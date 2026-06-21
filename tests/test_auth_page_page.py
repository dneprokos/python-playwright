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
        
        # test.use({
        #     httpCredentials: {
        #         username: 'admin',
        #         password: 'admin'
        #     }
        # });

        # //Alternatively, you can use request inside of the test in order to authenticate
        # // const response = await page.request.get('https://example.com/protected-page', {
        # //      headers: {
        # //         Authorization: `Basic ${Buffer.from('username:password').toString('base64')}`
        # //     }
        # // });

        # test('Verify successful login', async ({ baseURL, mainPage, basicAuthPage }) => {

        #     //Act
        #     await mainPage.navigateUrl(new PageDataConstants(baseURL as string).basicAuthPage.getUrlPath());
        #     await mainPage.waitForPageLoad();

        #     //Assert
        #     expect(await basicAuthPage.getPageHeader()).toBe('Basic Auth');
        #     expect((await basicAuthPage.getParagraphText()).trim()).toBe('Congratulations! You must have the proper credentials.');
        # });

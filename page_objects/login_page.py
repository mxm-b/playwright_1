import pytest
from playwright.sync_api import Page, expect
from faker import Faker

from page_objects.main_page import MainPage


class LoginPage(MainPage):
    def __init__(self, page):
        super().__init__(page)

    def insert_email(self):
        email = self.generate_email()
        self.page.get_by_test_id('login-username').fill(email)

    def insert_password(self):
        password = self.generate_password()
        self.page.get_by_test_id('login-password').fill(password)

    def click_confirm(self):
        button = self.page.get_by_role('button', name='Confirm')
        button.click()
        expect(self.page.get_by_test_id('login-submit-spinner')).to_be_visible()

    def check_error(self):
        expect(
            self.page.get_by_test_id(
                'login-error-inline'
            )
        ).to_have_text(
                'Invalid login or password.'
            )

    def generate_email(self):
        fake_email = Faker().email()
        return fake_email

    def generate_password(self):
        fake_password = Faker().password()
        return fake_password
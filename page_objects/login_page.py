from calendar import error

import pytest
from playwright.sync_api import Page, expect

from page_objects.main_page import MainPage


class LoginPage(MainPage):

    def insert_email(self, email):
        self.page.get_by_test_id('login-username').fill(email)

    def insert_password(self, password):
        self.page.get_by_test_id('login-password').fill(password)

    def click_confirm(self):
        button = self.page.get_by_test_id('login-submit')
        button.click()

    def check_loading_status(self):
        return self.page.get_by_test_id('login-submit-spinner')

    def receive_error_text(self):
        return self.page.get_by_test_id('login-error-inline')
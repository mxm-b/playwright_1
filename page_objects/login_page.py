from calendar import error

import pytest
from playwright.sync_api import Page, expect

from page_objects.main_page import MainPage


class LoginPage(MainPage):

    def __init__(self, page):
        super().__init__(page)
        self.loading_spinner = self.page.get_by_test_id('login-submit-spinner')

    def insert_email(self, email):
        self.page.get_by_test_id('login-username').fill(email)

    def insert_password(self, password):
        self.page.get_by_test_id('login-password').fill(password)

    def click_confirm(self):
        button = self.page.get_by_test_id('login-submit')
        button.click()

    def check_loading_status(self):
        return self.loading_spinner.is_visible()

    def wait_for_loading_finished(self):
        return self.loading_spinner.wait_for(state='hidden')

    def receive_error_text(self):
        return self.page.get_by_test_id('login-error-inline').inner_text()
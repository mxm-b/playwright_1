from calendar import error

import pytest
from playwright.sync_api import Page, expect

from page_objects.main_page import MainPage


class LoginPage(MainPage):

    def __init__(self, page):
        super().__init__(page)
        self.loading_spinner = self.page.get_by_test_id('login-submit-spinner')
        self.email_input_field = self.page.get_by_test_id('login-username')
        self.password_input_field = self.page.get_by_test_id('login-password')
        self.submit_button = self.page.get_by_test_id('login-submit')
        self.error_field = self.page.get_by_test_id('login-error-inline')

    def insert_email(self, email):
        self.email_input_field.fill(email)

    def insert_password(self, password):
        self.password_input_field.fill(password)

    def click_confirm(self):
        self.submit_button.click()

    def check_loading_status(self):
        return self.loading_spinner.is_visible()

    def wait_for_loading_finished(self):
        self.loading_spinner.wait_for(state='hidden')

    def get_error_text(self):
        return self.error_field.inner_text()
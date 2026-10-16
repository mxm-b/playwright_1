import pytest
from playwright.sync_api import Page, expect


class MainPage:
    def __init__ (self, page):
        self.page = page

    def click_login(self):
        self.page.get_by_test_id('nav-login').click()
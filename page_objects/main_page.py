import pytest
from playwright.sync_api import Page, expect


class MainPage:
    def __init__ (self, page):
        self.page = page

    def open(self):
        self.page.goto('http://2.26.162.45:8080/')

    def click_login(self):
        self.page.get_by_text('Login').click()
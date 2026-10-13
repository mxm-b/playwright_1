import pytest
from playwright.sync_api import Page, expect
from faker import Faker
import time

#from page_objects.main_page import *
from page_objects.login_page import *


def test_open_main_page(page: Page):
    page1 = MainPage(page)
    page1.open()

def test_login_button(page: Page):
    page2 = MainPage(page)
    page2.open()
    page2.click_login()

def test_login_auth(page: Page):
    page3 = MainPage(page)
    page3.open()
    page3.click_login()

    page4 = LoginPage(page)
    page4.insert_email()
    page4.insert_password()
    page4.click_confirm()
    page4.check_error()


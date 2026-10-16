import pytest
from playwright.sync_api import Page, expect
from faker import Faker
import time

from page_objects.login_page import LoginPage, MainPage


def test_login_auth(page: Page):
    fake = Faker()

    url_for_test = 'http://2.26.162.45:8080/'

    page.goto(url_for_test)
    main_page = MainPage(page)
    main_page.click_login()

    login_page = LoginPage(page)
    email1 = fake.email()
    password1 = fake.password()
    error_text = 'Invalid login or password.'

    login_page.insert_email(email1)
    login_page.insert_password(password1)
    login_page.click_confirm()
    login_page.wait_for_loading_finished()

    actual_error_text = login_page.get_error_text()
    assert actual_error_text == error_text, (
        f'Actual: {actual_error_text}, Expected: {error_text}'
    )
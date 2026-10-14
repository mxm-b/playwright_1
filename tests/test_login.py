import pytest
from playwright.sync_api import Page, expect
from faker import Faker
import time

from page_objects.login_page import LoginPage, MainPage
from db.fake_data import FakeData


def test_login_auth(page: Page):
    main_page = MainPage(page)
    main_page.open()
    main_page.click_login()

    login_page = LoginPage(page)
    fake_data = FakeData()
    email1 = fake_data.generate_email()
    password1 = fake_data.generate_password()
    error_text = 'Invalid login or password.'

    login_page.insert_email(email1)
    login_page.insert_password(password1)
    login_page.click_confirm()
    expect(page.get_by_test_id('login-submit-spinner')).to_be_visible()
    expect(page.get_by_test_id('login-error-inline')).to_have_text(error_text)
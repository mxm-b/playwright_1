from playwright.sync_api import Page
import pytest

from page_objects.basic_auth_page import BasicAuthPage
from ui.page_actions import PageActions


@pytest.mark.parametrize(
    'context',
    [('admin', 'admin')],
    indirect=True
)
@pytest.mark.parametrize(
    'URL, expect_message',
    [
        (
            'http://the-internet.herokuapp.com/basic_auth',
            'Congratulations! You must have the proper credentials.'
        )
    ]
)
def test_basic_auth(page: Page, URL, expect_message):
    basic_page = BasicAuthPage(page)
    page_actions = PageActions(page)

    page_actions.open_page(URL)
    received_message = basic_page.get_success_message()
    assert received_message == expect_message, \
        (
            f'Actual message: {received_message}, '
            f'Expected message: {expect_message}'
        )
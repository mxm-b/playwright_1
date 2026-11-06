from playwright.sync_api import Page, expect
import pytest
from logger import setup_logger

from page_objects.basic_auth_page import BasicAuthPage

logger = setup_logger()

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

    basic_page.open_page(URL)
    received_message = basic_page.get_success_message()
    assert received_message == expect_message, \
        (
            f'Actual message: {received_message}, '
            f'Expected message: {expect_message}'
        )
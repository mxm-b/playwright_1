from playwright.sync_api import Page, expect
from page_objects.windows_page import WindowsPage
from logger import setup_logger


logger = setup_logger()


def test_windows(page):
    windows_page = WindowsPage(page)
    url = 'https://the-internet.herokuapp.com/windows'
    expected_text = 'New Window'

    windows_page.open_page(url)
    new_page = windows_page.click_to_open_link()
    new_window = WindowsPage(new_page)
    new_window.choose_this_page()
    actual_text = new_window.get_text()
    assert actual_text == expected_text, \
        (
            f'Actual: {actual_text}\n'
            f'Expected: {expected_text}'
        )

    windows_page.choose_this_page()
    new_page2 = windows_page.click_to_open_link()
    new_window2 = WindowsPage(new_page2)
    new_window2.choose_this_page()
    actual_text_new_page_2 = new_window2.get_text()
    assert actual_text_new_page_2 == expected_text, \
        (
            f'Actual: {actual_text_new_page_2}\n'
            f'Expected: {expected_text}'
        )

    windows_page.choose_this_page()
    new_window.close_page()
    new_window2.close_page()
    quantity_of_opened_pages = len(page.context.pages)
    assert quantity_of_opened_pages == 1, \
        (
            f'Actual: {quantity_of_opened_pages}\n'
            f'Expected: {1}'
        )
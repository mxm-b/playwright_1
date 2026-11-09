from playwright.sync_api import Page, expect
from page_objects.windows_page import WindowsPage
from ui.page_actions import PageActions
from logger import setup_logger


logger = setup_logger()


def test_windows(page):
    windows_page = WindowsPage(page)
    page_actions = PageActions(page)
    url = 'https://the-internet.herokuapp.com/windows'
    expected_text = 'New Window'

    page_actions.open_page(url)
    with page_actions.expect_new_page() as page_info:
        windows_page.click_to_open_link()

    new_page = page_info.value

    new_window = WindowsPage(new_page)
    new_page_actions = PageActions(new_page)
    new_page_actions.choose_page()
    actual_text = new_window.get_text_from_clicked_link()
    assert actual_text == expected_text, \
        (
            f'Actual: {actual_text}\n'
            f'Expected: {expected_text}'
        )

    page_actions.choose_page()
    with page_actions.expect_new_page() as page_info_2:
        windows_page.click_to_open_link()

    new_page_2 = page_info_2.value

    new_window_2 = WindowsPage(new_page_2)
    new_page_actions_2 = PageActions(new_page_2)
    new_page_actions_2.choose_page()
    actual_text_new_page_2 = new_window_2.get_text_from_clicked_link()
    assert actual_text_new_page_2 == expected_text, \
        (
            f'Actual: {actual_text_new_page_2}\n'
            f'Expected: {expected_text}'
        )

    page_actions.choose_page()
    new_page_actions.close_page()
    new_page_actions_2.close_page()
    quantity_of_opened_pages = len(page.context.pages)
    assert quantity_of_opened_pages == 1, \
        (
            f'Actual: {quantity_of_opened_pages}\n'
            f'Expected: {1}'
        )
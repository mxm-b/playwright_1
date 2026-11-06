from playwright.sync_api import Page, expect
from logger import setup_logger
from page_objects.context_click_page import ContextClickPage

logger = setup_logger()

def test_context_click(page):

    URL = 'https://the-internet.herokuapp.com/context_menu'
    context_page = ContextClickPage(page)
    expected_alert_text = 'You selected a context menu'
    dialog_messages = []

    def handle_dialog(dialog):
        dialog_messages.append(dialog.message)
        dialog.accept()

    page.once("dialog", handle_dialog)

    context_page.open_page(URL)
    context_page.click_right_on_box()
    assert dialog_messages[0] == expected_alert_text, \
        (
            f'Actual: {dialog_messages[0]}\n'
            f'Expected: {expected_alert_text}'
        )
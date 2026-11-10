from page_objects.context_click_page import ContextClickPage
from ui.page_actions import PageActions


def test_context_click(page):
    url = 'https://the-internet.herokuapp.com/context_menu'
    context_page = ContextClickPage(page)
    page_actions = PageActions(page)
    expected_alert_text = 'You selected a context menu'

    page_actions.open_page(url)
    received_alert_text = page_actions._handle_dialog(
        context_page.click_right_on_box,
        mode='accept'
    )
    assert received_alert_text == expected_alert_text, \
        (
            f'Actual: {received_alert_text}\n'
            f'Expected: {expected_alert_text}'
        )
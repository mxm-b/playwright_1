from logger import setup_logger
from faker import Faker
from page_objects.alert_page import AlertPage
from ui.page_actions import PageActions


logger = setup_logger()
faker = Faker()


def test_alert(page):

    url = 'https://the-internet.herokuapp.com/javascript_alerts'
    page_actions = PageActions(page)
    alert_page = AlertPage(page)
    dialog_messages = []
    random_text = faker.sentence()
    alert_expected_message = 'You successfully clicked an alert'
    confirm_expected_message = 'You clicked: Ok'
    prompt_expected_message = f'You entered: {random_text}'
    alert_expected_alert_text = "I am a JS Alert"
    confirm_expected_alert_text = "I am a JS Confirm"
    prompt_expected_alert_text = "I am a JS prompt"

    def handle_dialog(dialog):
        dialog_messages.append(dialog.message)
        if dialog.type == 'prompt':
            dialog.accept(random_text)
        else:
            dialog.accept()

    page.on("dialog", handle_dialog)

    page_actions.open_page(url)
    alert_page.click_alert()
    received_text = alert_page.get_result_text()
    assert dialog_messages[0] == alert_expected_alert_text, \
        (
            f'Actual: {dialog_messages[0]}\n'
            f'Expected: {alert_expected_alert_text}'
        )
    assert received_text == alert_expected_message, \
        (
            f'Actual: {received_text}\n'
            f'Expected: {alert_expected_message}'
        )

    alert_page.click_confirm()
    received_text = alert_page.get_result_text()
    assert dialog_messages[1] == confirm_expected_alert_text, \
        (
            f'Actual: {dialog_messages[1]}\n'
            f'Expected: {confirm_expected_alert_text}'
        )
    assert received_text == confirm_expected_message, \
        (
            f'Actual: {received_text}\n'
            f'Expected: {confirm_expected_message}'
        )

    alert_page.click_prompt()
    received_text = alert_page.get_result_text()
    assert dialog_messages[2] == prompt_expected_alert_text, \
        (
            f'Actual: {dialog_messages[2]}\n'
            f'Expected: {prompt_expected_alert_text}'
        )
    assert received_text == prompt_expected_message, \
        (
            f'Actual: {received_text}\n'
            f'Expected: {prompt_expected_message}'
        )
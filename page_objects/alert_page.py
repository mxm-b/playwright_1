from playwright.sync_api import Page
from ui.web_element import WebElement


class AlertPage:
    def __init__(self, page):
        self.page = page
        self.button_alert = WebElement(
        page.get_by_role('button', name='Click for JS Alert'),
        'click on button "Click for JS Alert"',
        page
        )
        self.button_confirm = WebElement(
            page.get_by_role('button', name='Click for JS Confirm'),
            'click on button "Click for JS Confirm"',
            page
        )
        self.button_prompt = WebElement(
            page.get_by_role('button', name='Click for JS Prompt'),
            'click on button "Click for JS Prompt"',
            page
        )
        self.success_message = WebElement(
            page.locator('#result'),
            'result message',
            page
        )

    def click_alert(self):
        self.button_alert.click()

    def click_confirm(self):
        self.button_confirm.click()

    def click_prompt(self):
        self.button_prompt.click()

    def get_result_text(self):
        return self.success_message.get_inner_text()
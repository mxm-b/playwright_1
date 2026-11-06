from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class AlertPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)

        self.button_alert_locator = page.get_by_role('button', name='Click for JS Alert')
        self.button_alert_element = WebElement(
        self.button_alert_locator,
        f'click on button: {self.button_alert_locator}',
        page
        )

        self.button_confirm_locator = page.get_by_role('button', name='Click for JS Confirm')
        self.button_confirm_element = WebElement(
            self.button_confirm_locator,
            f'click on button: {self.button_confirm_locator}',
            page
        )

        self.button_prompt_locator = page.get_by_role('button', name='Click for JS Prompt')
        self.button_prompt_element = WebElement(
            self.button_prompt_locator,
            f'click on button: {self.button_prompt_locator}',
            page
        )

        self.success_message = page.locator('#result')
        self.success_message_element = WebElement(
            self.success_message,
            'result message',
            page
        )

    def open_page(self, url):
        return self.actions.open_page(url)

    def click_alert(self):
        return self.button_alert_element.click()

    def click_confirm(self):
        return self.button_confirm_element.click()

    def click_prompt(self):
        return self.button_prompt_element.click()

    def get_result_text(self):
        return self.success_message_element.get_inner_text()
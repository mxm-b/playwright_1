from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class BasicAuthPage:
    def __init__(self, page):
        self.page = page
        self.success_message_locator = self.page.locator('#content p')
        self.success_message_web_element = WebElement(
            self.success_message_locator,
            'successful auth message',
            page
        )
        self.actions = PageActions(page)

    def open_page(self, url):
        return self.actions.open_page(url)

    def get_success_message(self):
        return self.success_message_web_element.get_inner_text()
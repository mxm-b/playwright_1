from playwright.sync_api import Page
from ui.web_element import WebElement


class BasicAuthPage:
    def __init__(self, page):
        self.page = page
        self.success_message = WebElement(
            self.page.locator('#content p'),
            'successful auth message',
            page
        )

    def get_success_message(self):
        return self.success_message.get_inner_text()
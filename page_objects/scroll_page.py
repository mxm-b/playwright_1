from asyncio import wait_for

from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class ScrollPage:
    def __init__(self,page):
        self.page = page
        self.actions = PageActions(page)

        self.paragraph_locator = self.page.locator('.jscroll-added')
        self.paragraph_element = WebElement(
            self.paragraph_locator,
            'paragraph object',
            page
        )

    def open_page(self, url):
        self.actions.open_page(url)

    def scroll_down(self):
        self.actions.scroll_page()

    def count_paragraphs(self):
        return self.paragraph_element.count_elements()
from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class ContextClickPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)

        self.dashed_box_locator = self.page.locator('#hot-spot')
        self.dashed_box_element = WebElement(
            self.dashed_box_locator,
            'box to click',
            page
        )

    def open_page(self, url):
        return self.actions.open_page(url)

    def click_right_on_box(self):
        return self.dashed_box_element.right_click()

from playwright.sync_api import Page
from ui.web_element import WebElement


class ContextClickPage:
    def __init__(self, page):
        self.page = page
        self.dashed_box = WebElement(
            self.page.locator('#hot-spot'),
            'box to click',
            page
        )

    def click_right_on_box(self):
        return self.dashed_box.right_click()

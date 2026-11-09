from playwright.sync_api import Page
from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page):
        self.page = page
        self.link_to_click = WebElement(
            self.page.locator('.example a'),
            'clickable link',
            page
        )
        self.text_from_clicked_link = WebElement(
            self.page.locator('.example h3'),
            'receive text from new page',
            page
        )

    def click_to_open_link(self):
        self.link_to_click.click()

    def get_text_from_clicked_link(self):
        return self.text_from_clicked_link.get_inner_text()


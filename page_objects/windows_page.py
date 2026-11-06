from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.link_locator = self.page.locator('.example a')
        self.link_element = WebElement(
            self.link_locator,
            'clickable link',
            page
        )

        self.text_from_clicked_link_locator = self.page.locator('.example h3')
        self.text_from_clicked_link_element = WebElement(
            self.text_from_clicked_link_locator,
            'receive text from new page',
            page
        )

    def open_page(self, url):
        self.actions.open_page(url)

    def click_to_open_link(self):
        with self.actions.expect_new_page() as new_page:
            self.link_element.click()
        return new_page.value

    def close_page(self):
        self.actions.close_page()

    def choose_this_page(self):
        self.actions.choose_page()

    def get_text(self):
        return self.text_from_clicked_link_element.get_inner_text()


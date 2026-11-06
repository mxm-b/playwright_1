from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.page_actions import PageActions


class FramesPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)

        self.top_frame_locator = self.page.frame_locator("frame[name='frame-top']")
        self.left_frame_locator = self.top_frame_locator.frame_locator("frame[name='frame-left']")
        self.left_frame_body_locator = self.left_frame_locator.locator('body')
        self.left_frame_element = WebElement(
            self.left_frame_body_locator,
            'text of left frame',
            page
        )
        self.middle_frame_locator = self.top_frame_locator.frame_locator("frame[name='frame-middle']")
        self.middle_frame_body_locator = self.middle_frame_locator.locator('body')
        self.middle_frame_element = WebElement(
            self.middle_frame_body_locator,
            'text of middle frame',
            page
        )
        self.right_frame_locator = self.top_frame_locator.frame_locator("frame[name='frame-right']")
        self.right_frame_body_locator = self.right_frame_locator.locator('body')
        self.right_frame_element = WebElement(
            self.right_frame_body_locator,
            'text of right frame',
            page
        )
        self.bottom_frame_locator = self.page.frame_locator("frame[name='frame-bottom']")
        self.bottom_frame_body_locator = self.bottom_frame_locator.locator('body')
        self.bottom_frame_element = WebElement(
            self.bottom_frame_body_locator,
            'text of bottom frame',
            page
        )

    def open_page(self, url):
        self.actions.open_page(url)

    def get_text_left_frame(self):
        return self.left_frame_element.get_inner_text()

    def get_text_middle_frame(self):
        return self.middle_frame_element.get_inner_text()

    def get_text_right_frame(self):
        return self.right_frame_element.get_inner_text()

    def get_text_bottom_frame(self):
        return self.bottom_frame_element.get_inner_text()


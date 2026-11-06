from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class HoversPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)
        self.user_locator = self.page.get_by_alt_text('User Avatar')
        self.user_card_locator = self.page.locator('.figure')
        self.name_locator = self.user_card_locator.locator('h5')

    def open_page(self, url):
        self.actions.open_page(url)

    def count_users(self):
        return self.user_card_locator.count()

    def hover_cursor(self, index):
        user_locator = self.user_locator.nth(index)
        user_avatar_element = WebElement(
            user_locator,
            'chosen card',
            self.page
        )
        user_avatar_element.hover_cursor()

    def get_name_of_user(self, index):
        user_name_locator = self.name_locator.nth(index)
        user_name_element = WebElement(
            user_name_locator,
            'user name',
            self.page
        )
        return user_name_element.get_inner_text()


from playwright.sync_api import Page
from ui.multiweb_element import MultiWebElement


class HoversPage:
    def __init__(self, page):
        self.page = page
        self.user_avatars = MultiWebElement(
            self.page,
            self.page.get_by_alt_text('User Avatar'),
            'all user avatars'
        )
        self.names_of_users = MultiWebElement(
            self.page,
            self.page.locator('.figure h5'),
            'names of users'
        )

    def count_users(self):
        return self.user_avatars.count()

    def hover_cursor(self, index):
        self.user_avatars.nth(index).hover_cursor()

    def get_name_of_user(self, index):
        return self.names_of_users.nth(index).get_inner_text()
from playwright.sync_api import Page
from ui.multiweb_element import MultiWebElement


class DynamicContentPage:
    def __init__(self, page):
        self.page = page
        self.photos = MultiWebElement(
            self.page,
            self.page.locator('#content img'),
            'all photo elements',
        )

    def get_attribute_of_photo(self, index):
        return self.photos.nth(index).get_attribute('src')
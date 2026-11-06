from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.page_actions import PageActions


class DynamicContentPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)

        self.photo_locator = self.page.locator('#content img')


    def open_page(self, url):
        self.actions.open_page(url)

    def reload_page(self):
        self.actions.reload_page()

    def get_attribute_of_photo(self, index):
        numbered_photo = self.photo_locator.nth(index)
        photo_element = WebElement(
            numbered_photo,
            'photo element',
            self.page
        )
        return photo_element.get_attribute('src')
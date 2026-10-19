from playwright.sync_api import Page


class StarterPage:

    def __init__(self, page):
        self.page = page
        self.search_bar = self.page.get_by_test_id('search-input')

    '''def click_search_bar(self):
        self.search_bar.click()'''

    def enter_text_to_search(self, text):
        self.search_bar.fill(text)
        self.search_bar.press('Enter')


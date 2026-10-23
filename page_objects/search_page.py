from page_objects.starter_page import StarterPage

from enum import StrEnum


class Filters(StrEnum):
    BY_RELEVANCE = 'Relevance'
    BY_PRICE_ASC = 'Price: low to high'
    BY_PRICE_DESC = 'Price: high to low'
    BY_READ_SHORT = 'Read time: shortest first'
    BY_READ_LONG = 'Read time: longest first'
    BY_TITLE = 'Title (A-Z)'


class SearchPage(StarterPage):

    def __init__(self, page):
        super().__init__(page)
        self.filter_by_sort = self.page.get_by_test_id('filter-sort')
        self.apply_button = self.page.get_by_test_id('apply-filters-button')
        self.find_price_class = self.page.locator('.article-price')
        self.spinner = self.page.get_by_test_id('results-loader-svg')

    def set_filter(self, filter_type):
        self.filter_by_sort.select_option(label=filter_type)
        self.apply_button.click()

    def search_price_for_articles(self, n):
        price_list = []
        prices = self.find_price_class.all()[:n]
        for price in prices:
            price_list.append(int(price.get_attribute('data-price')))
        return price_list

    def wait_for_loading_finished(self):
        self.spinner.wait_for(state='visible')
        self.spinner.wait_for(state='hidden')


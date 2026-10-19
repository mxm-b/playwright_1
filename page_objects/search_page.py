from page_objects.starter_page import StarterPage

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
        return self.find_price_class.all_inner_texts()[:n]

    def wait_for_loading_finished(self):
        self.spinner.wait_for(state='hidden')


import pytest
from playwright.sync_api import Page

from page_objects.search_page import SearchPage
from page_objects.starter_page import StarterPage
from config_reader import ConfigReader


config_reader = ConfigReader()
tests = config_reader.get_tests()

@pytest.mark.parametrize('test_data', tests)
def test_receive_prices(page:Page, test_data):

    testing_url = 'http://2.26.162.45:8080'

    text_to_search = test_data['name']
    quantity = test_data['n']
    filter_type = test_data['filter_type']
    correct_prices = []


    page.goto(testing_url)
    starter_page = StarterPage(page)
    starter_page.enter_text_to_search(text_to_search)


    search_page = SearchPage(page)
    search_page.wait_for_loading_finished()
    search_page.set_filter(filter_type)
    search_page.wait_for_loading_finished()
    prices = search_page.search_price_for_articles(quantity)

    for price in prices:
        correct_prices.append(
            int(price.replace('RUB', '').replace(' ', ''))
        )
        print(price)

    if filter_type == 'Price: low to high':
        assert correct_prices == sorted(correct_prices)
    else:
        assert correct_prices == sorted(correct_prices, reverse=True)

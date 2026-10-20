import pytest
from playwright.sync_api import Page

from page_objects.search_page import SearchPage, Filters
from page_objects.starter_page import StarterPage
from config_reader import ConfigReader


config_reader = ConfigReader('config.json')

@pytest.mark.parametrize('test_data',
    [{
      "name": "city",
      "n": 10,
      "filter_type": "Price: low to high"
    },
    {
      "name": "city",
      "n": 15,
      "filter_type": "Price: high to low"
    },
    {
      "name": "habits",
      "n": 10,
      "filter_type": "Price: low to high"
    },
    {
      "name": "habits",
      "n": 15,
      "filter_type": "Price: high to low"
    }]
  )
def test_receive_prices(page:Page, test_data):

    page.goto(config_reader.get_url())
    starter_page = StarterPage(page)
    starter_page.enter_text_to_search(test_data['name'])


    search_page = SearchPage(page)
    search_page.set_filter(test_data['filter_type'])
    search_page.wait_for_loading_finished()
    prices = search_page.search_price_for_articles(test_data['n'])


    if test_data['filter_type'] == Filters.BY_PRICE_ASC:
        assert prices == sorted(prices), (
            f'Actual: {prices}, Expected: {sorted(prices)}'
        )
    elif test_data['filter_type'] == Filters.BY_PRICE_DESC:
        assert prices == sorted(prices, reverse=True), (
            f'Actual: {prices}, Expected: {sorted(prices, reverse=True)}'
        )
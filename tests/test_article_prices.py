import pytest
from playwright.sync_api import Page

from page_objects.search_page import SearchPage, Filters
from page_objects.starter_page import StarterPage
from config_reader import ConfigReader


config_reader = ConfigReader('config.json')

@pytest.mark.parametrize('name', ['city', 'habits'])
@pytest.mark.parametrize(
    'n, filter_type', [
        (10, Filters.BY_PRICE_ASC),
        (15, Filters.BY_PRICE_DESC)
    ]
)

def test_receive_prices(page:Page, name, n, filter_type):

    page.goto(config_reader.get_url())
    starter_page = StarterPage(page)
    starter_page.enter_text_to_search(name)


    search_page = SearchPage(page)
    search_page.set_filter(filter_type)
    search_page.wait_for_loading_finished()
    prices = search_page.search_price_for_articles(n)


    if filter_type == Filters.BY_PRICE_ASC:
        assert prices == sorted(prices), (
            f'Actual: {prices}, Expected: {sorted(prices)}'
        )
    elif filter_type == Filters.BY_PRICE_DESC:
        assert prices == sorted(prices, reverse=True), (
            f'Actual: {prices}, Expected: {sorted(prices, reverse=True)}'
        )
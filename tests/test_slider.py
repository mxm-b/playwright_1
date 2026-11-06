import random
from playwright.sync_api import Page, expect
from logger import setup_logger
from page_objects.slider_page import SliderPage


logger = setup_logger()


def test_slider(page):
    url = 'https://the-internet.herokuapp.com/horizontal_slider'
    slider_page = SliderPage(page)
    key = 'ArrowRight'
    random_value_click = random.randint(1, 9)
    expected_value = random_value_click * 0.5

    slider_page.open_page(url)
    slider_page.move_slider_with_value(random_value_click, key)
    printed_value = slider_page.receive_slider_value()
    assert expected_value == printed_value, \
        (
            f'Actual: {printed_value}\n'
            f'Expected: {expected_value}'
        )


import random
from logger import setup_logger
from page_objects.slider_page import SliderPage
from ui.page_actions import PageActions


logger = setup_logger()


def test_slider(page):
    url = 'https://the-internet.herokuapp.com/horizontal_slider'
    slider_page = SliderPage(page)
    page_actions = PageActions(page)
    key = 'ArrowRight'

    page_actions.open_page(url)

    min_value = slider_page.get_min_value()
    max_value = slider_page.get_max_value()
    step_value = slider_page.get_step_value()

    number_of_steps = int((max_value - min_value) / step_value)
    random_clicks = random.randint(1, number_of_steps - 1)
    expected_value = min_value + random_clicks * step_value

    slider_page.move_slider_with_value(random_clicks, key)
    printed_value = slider_page.receive_slider_value()
    assert expected_value == printed_value, \
        (
            f'Actual: {printed_value}\n'
            f'Expected: {expected_value}'
        )


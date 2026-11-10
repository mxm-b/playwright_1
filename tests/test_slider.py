import random
from page_objects.slider_page import SliderPage
from ui.page_actions import PageActions


def test_slider(page):
    url = 'https://the-internet.herokuapp.com/horizontal_slider'
    slider_page = SliderPage(page)
    page_actions = PageActions(page)

    page_actions.open_page(url)

    min_value = slider_page.get_min_value()
    max_value = slider_page.get_max_value()
    step_value = slider_page.get_step_value()

    total_number_of_steps = int((max_value - min_value) / step_value)
    index_step = random.randint(1, total_number_of_steps - 1)
    target_value = min_value + index_step * step_value
    slider_page.move_slider_with_value(target_value)
    printed_value = slider_page.receive_slider_value()
    assert target_value == printed_value, \
        (
            f'Actual: {printed_value}\n'
            f'Expected: {target_value}'
        )


from playwright.sync_api import Page
from ui.web_element import WebElement
import random


class SliderPage:
    def __init__(self, page):
        self.page = page
        self.slider = WebElement(
            self.page.get_by_role('slider'),
            'slider to choose the value',
            page
        )
        self.slider_value = WebElement(
            self.page.locator('#range'),
            'chosen value on slider',
            page
        )

    def move_slider_with_value(self, number_of_clicks, key):
        for slider_mover in range(number_of_clicks):
            self.slider.press_key(key)

    def receive_slider_value(self):
        return float(self.slider_value.get_inner_text())

    def get_min_value(self):
        return float(self.slider.get_attribute('min'))

    def get_max_value(self):
        return float(self.slider.get_attribute('max'))

    def get_step_value(self):
        return float(self.slider.get_attribute('step'))
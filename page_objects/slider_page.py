from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement
import random


class SliderPage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)

        self.slider_locator = self.page.get_by_role('slider')
        self.slider_element = WebElement(
            self.slider_locator,
            'slider to choose the value',
            page
        )
        self.slider_value_locator = self.page.locator('#range')
        self.slider_value_element = WebElement(
            self.slider_value_locator,
            'chosen value on slider',
            page
        )


    def open_page(self, url):
        self.actions.open_page(url)

    def move_slider_with_value(self, number_of_clicks, key):
        for slider_mover in range(number_of_clicks):
            self.slider_element.press_key(key)

    def receive_slider_value(self):
        return float(self.slider_value_element.get_inner_text())
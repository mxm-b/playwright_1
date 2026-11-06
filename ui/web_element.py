import logging
from playwright.sync_api import Locator, Page
from logger import LOGGER_NAME
from pathlib import Path


logger = logging.getLogger(LOGGER_NAME)


class WebElement:
    def __init__(self, locator: Locator, description: str, page: Page):
        self.page = page
        self.locator = locator
        self.description = description

    def get_inner_text(self) -> str:
        logger.info(f'{self}- getting inner text')
        result = self.locator.inner_text()
        logger.info(f'{self} - inner text: {result}')
        return result

    def click(self):
        logger.info(f'{self}- click')
        self.locator.click()

    def insert_text(self, text):
        logger.info(f'{self}- inserting text: {text}')
        self.locator.fill(text)

    def right_click(self):
        logger.info(f'{self}- right click')
        self.locator.click(button='right')

    def press_key(self, key):
        logger.info(f'{self}- press key: {key}')
        self.locator.press(key)

    def hover_cursor(self):
        logger.info(f'{self}- hover coursor')
        self.locator.hover()

    def count_elements(self):
        logger.info(f'{self}- count elements')
        return self.locator.count()

    def get_attribute(self, name):
        logger.info(f'{self}- get attribute')
        return self.locator.get_attribute(name)

    def scroll_element_into_view(self,index):
        logger.info(f'{self}- scroll down to element with index {index}')
        self.locator.nth(index).scroll_into_view_if_needed()

    def set_input_files(self, file_path: Path):
        logger.info(f'{self}- set input file "{file_path}"')
        self.locator.set_input_files(file_path)
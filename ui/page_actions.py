import logging
from playwright.sync_api import Page
from logger import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)


class PageActions:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url: str):
        logger.info(f'Go to page: {url}')
        self.page.goto(url)

    def expect_new_page(self):
        logger.info('Expect new page')
        return self.page.context.expect_page()

    def close_page(self) -> None:
        logger.info('Close current page')
        self.page.close()

    def choose_page(self):
        logger.info('Choose another page')
        self.page.bring_to_front()

    def reload_page(self):
        logger.info('Reload page')
        self.page.reload()

    def scroll_page(self):
        logger.info('Scroll page')
        self.page.mouse.wheel(0,500)

    def expect_download(self):
        logger.info('Expect download')
        return self.page.expect_download()
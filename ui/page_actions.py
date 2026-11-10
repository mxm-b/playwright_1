import logging
from typing import Callable


from playwright.sync_api import Page, Dialog
from logger import LOGGER_NAME
from ui.multiweb_element import MultiWebElement
from ui.web_element import WebElement


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

    def scroll_into_view_if_needed(self, element: WebElement):
        logger.info(f'Scroll page to element {element.description}')
        element.locator.scroll_into_view_if_needed()

    def expect_download(self):
        logger.info('Expect download')
        return self.page.expect_download()

    def _handle_dialog(
            self,
            action: Callable[[], None],
            mode: str,
            prompt_text: str | None = None,
    ) -> str:
        logger.info('PageActions: expect dialog')
        message = ''

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            logger.info(f'PageActions: dialog {dialog.type} with message {message}')
            if mode == 'dismiss':
                dialog.dismiss()
                return

            if prompt_text is None:
                dialog.accept()
                return

            dialog.accept(prompt_text)

        self.page.once('dialog', handle_dialog)
        action()

        if not message:
            raise RuntimeError(f'Expected dialog was not shown')

        return message
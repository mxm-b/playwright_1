from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class DownloadPage:
    def __init__(self,page):
        self.page = page
        self.actions = PageActions(page)
        self.file_name_locator = self.page.locator('.example a')

    def open_page(self, url):
        self.actions.open_page(url)

    def get_name_of_file(self, index):
        numbered_file = self.file_name_locator.nth(index)
        file_name_element = WebElement(
            numbered_file,
            'name of file',
            self.page
        )
        return file_name_element.get_inner_text()

    def download_file(self, index):
        file_locator = self.file_name_locator.nth(index)
        file_element = WebElement(
            file_locator,
            'file to download',
            self.page
        )
        with self.actions.expect_download() as download_info:
            file_element.click()
        return download_info.value
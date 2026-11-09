from playwright.sync_api import Page

from ui.multiweb_element import MultiWebElement
from ui.web_element import WebElement


class DownloadPage:
    def __init__(self,page):
        self.page = page
        self.file_names = MultiWebElement(
            self.page,
            self.page.locator('.example a'),
            'all file names'
        )

    def get_name_of_file(self, index):
        return self.file_names.nth(index).get_inner_text()

    def click_to_download_file(self, index):
        self.file_names.nth(index).click()
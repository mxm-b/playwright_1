from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.page_actions import PageActions


class UploadImagePage:
    def __init__(self, page):
        self.page = page
        self.actions = PageActions(page)

        self.file_input_locator = self.page.locator('#file-upload')
        self.file_input_element = WebElement(
            self.file_input_locator,
            'an input button to choose file to upload it',
            page
        )
        self.upload_button_locator = self.page.locator('#file-submit')
        self.upload_button_element = WebElement(
            self.upload_button_locator,
            'button to submit uploaded file',
            page
        )

        self.uploading_header_locator = self.page.locator('.example h3')
        self.uploading_header_element = WebElement(
            self.uploading_header_locator,
            'a successful uploading message',
            page
        )
        self.file_name_locator = self.page.locator('#uploaded-files')
        self.file_name_element = WebElement(
            self.file_name_locator,
            'name of uploaded file',
            page
        )

    def open_page(self, url):
        self.actions.open_page(url)

    def select_file_from_path(self, path):
        self.file_input_element.click()
        self.file_input_element.set_input_files(path)

    def click_upload_button(self):
        self.upload_button_element.click()

    def get_success_message(self):
        return self.uploading_header_element.get_inner_text()

    def get_file_name(self):
        return self.file_name_element.get_inner_text()

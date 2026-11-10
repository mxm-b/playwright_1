from playwright.sync_api import Page
from ui.web_element import WebElement


class UploadImagePage:
    def __init__(self, page):
        self.page = page
        self.file_input = WebElement(
            self.page.locator('#file-upload'),
            'an input button to choose file to upload it',
            page
        )
        self.upload_button = WebElement(
            self.page.locator('#file-submit'),
            'button to submit uploaded file',
            page
        )
        self.uploading_header = WebElement(
            self.page.locator('.example h3'),
            'a successful uploading message',
            page
        )
        self.file_name = WebElement(
            self.page.locator('#uploaded-files'),
            'name of uploaded file',
            page
        )

    def select_file_from_path(self, path):
        self.file_input.click()
        self.file_input.set_input_files(path)

    def click_upload_button(self):
        self.upload_button.click()

    def get_success_message(self):
        return self.uploading_header.get_inner_text()

    def get_file_name(self):
        return self.file_name.get_inner_text()

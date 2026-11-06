from playwright.sync_api import Page
from logger import setup_logger
from page_objects.upload_image_page import UploadImagePage


logger = setup_logger()


def test_upload_image(page):
    upload_image_page = UploadImagePage(page)
    url = 'https://the-internet.herokuapp.com/upload'
    file_name = '25_ru.jpg'
    path = f'/Users/max.bokarev/Downloads/{file_name}'
    success_message = 'File Uploaded!'

    upload_image_page.open_page(url)
    upload_image_page.select_file_from_path(path)
    upload_image_page.click_upload_button()

    received_success_message = upload_image_page.get_success_message()
    received_file_name = upload_image_page.get_file_name()
    assert received_success_message == success_message, \
        (
            f'Actual success message: {received_success_message}\n'
            f'Expected success message: {success_message}'
        )
    assert received_file_name == file_name, \
        (
            f'Actual file name: {received_file_name}\n'
            f'Received file name: {file_name}'
        )
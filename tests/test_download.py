from playwright.sync_api import Page
from logger import setup_logger
from page_objects.download_page import DownloadPage


logger = setup_logger()


def test_download_page(page):
    download_page = DownloadPage(page)
    url = 'https://the-internet.herokuapp.com/download'
    file_index = 3

    download_page.open_page(url)
    name_of_chosen_file = download_page.get_name_of_file(file_index - 1)
    name_of_downloaded_file = download_page.download_file(file_index - 1).suggested_filename
    assert name_of_chosen_file == name_of_downloaded_file, \
        (
            f'Actual file name: {name_of_downloaded_file}\n'
            f'Expected file name: {name_of_chosen_file}'
        )

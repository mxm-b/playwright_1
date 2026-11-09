from playwright.sync_api import Page
from logger import setup_logger
from page_objects.download_page import DownloadPage
from ui.page_actions import PageActions


logger = setup_logger()


def test_download_page(page):
    download_page = DownloadPage(page)
    page_actions = PageActions(page)
    url = 'https://the-internet.herokuapp.com/download'
    file_index = 3

    page_actions.open_page(url)
    name_of_chosen_file = download_page.get_name_of_file(file_index - 1)
    with page_actions.expect_download() as download_info:
        download_page.click_to_download_file(file_index - 1)
    name_of_downloaded_file = download_info.value.suggested_filename
    assert name_of_chosen_file == name_of_downloaded_file, \
        (
            f'Actual file name: {name_of_downloaded_file}\n'
            f'Expected file name: {name_of_chosen_file}'
        )
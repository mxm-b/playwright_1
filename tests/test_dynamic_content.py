from page_objects.dynamic_content_page import DynamicContentPage
from ui.page_actions import PageActions
from logger import setup_logger


logger = setup_logger()


def test_dynamic_content(page):
    dynamic_content_page = DynamicContentPage(page)
    page_actions = PageActions(page)
    url = 'https://the-internet.herokuapp.com/dynamic_content'
    photos_quantity = 3
    found_pair = False

    page_actions.open_page(url)
    while not found_pair:
        photos_list = []
        for photo_index in range(photos_quantity):
            photos_list.append(dynamic_content_page.get_attribute_of_photo(photo_index))
        found_pair = len(set(photos_list)) < len(photos_list)
        if not found_pair:
            page_actions.reload_page()
from page_objects.dynamic_content_page import DynamicContentPage
from logger import setup_logger


logger = setup_logger()


def test_dynamic_content(page):
    dynamic_content_page = DynamicContentPage(page)
    url = 'https://the-internet.herokuapp.com/dynamic_content'
    photos_quantity = 3
    found_pair = False

    dynamic_content_page.open_page(url)
    while not found_pair:
        photos_list = []
        for photo_index in range(photos_quantity):
            photos_list.append(dynamic_content_page.get_attribute_of_photo(photo_index))
        found_pair = (
            photos_list[0] == photos_list[1]
            or photos_list[0] == photos_list[2]
            or photos_list[1] == photos_list[2]
        )
        if not found_pair:
            dynamic_content_page.reload_page()
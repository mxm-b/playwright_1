from playwright.sync_api import Page
from page_objects.scroll_page import ScrollPage
from logger import setup_logger


logger = setup_logger()


def test_scroll_page(page):
    scroll_page = ScrollPage(page)
    url = 'https://the-internet.herokuapp.com/infinite_scroll'
    paragraph_counter = False

    scroll_page.open_page(url)
    while not paragraph_counter:
        paragraph_quantity = scroll_page.count_paragraphs()
        print(paragraph_quantity)
        if paragraph_quantity >= 10:
            paragraph_counter = True
        else:
            scroll_page.scroll_down()
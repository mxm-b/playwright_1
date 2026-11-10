from page_objects.scroll_page import ScrollPage
from ui.page_actions import PageActions


def test_scroll_page(page):
    scroll_page = ScrollPage(page)
    page_actions = PageActions(page)
    url = 'https://the-internet.herokuapp.com/infinite_scroll'
    paragraph_counter = False

    page_actions.open_page(url)
    while not paragraph_counter:
        paragraph_quantity = scroll_page.count_paragraphs()
        if paragraph_quantity >= 10:
            paragraph_counter = True
        else:
            page_actions.scroll_into_view_if_needed(scroll_page.get_last_paragraph())
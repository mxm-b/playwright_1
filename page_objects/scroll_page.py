from playwright.sync_api import Page
from ui.multiweb_element import MultiWebElement


class ScrollPage:
    def __init__(self,page):
        self.page = page
        self.paragraphs = MultiWebElement(
            self.page,
            self.page.locator('.jscroll-added'),
            'paragraph object'
        )

    def count_paragraphs(self):
        return self.paragraphs.count()

    def get_last_paragraph(self):
        return self.paragraphs.last()
from ui.web_element import WebElement


class FramesPage:
    def __init__(self, page):
        self.page = page

        self.left_frame_text = WebElement(
            self.page
            .frame_locator("frame[name='frame-top']")
            .frame_locator("frame[name='frame-left']")
            .locator('body'),
            'text of left frame',
            page
        )

        self.middle_frame_text = WebElement(
            self.page
            .frame_locator("frame[name='frame-top']")
            .frame_locator("frame[name='frame-middle']")
            .locator('body'),
            'text of middle frame',
            page
        )

        self.right_frame_text = WebElement(
            self.page
            .frame_locator("frame[name='frame-top']")
            .frame_locator("frame[name='frame-right']")
            .locator('body'),
            'text of right frame',
            page
        )

        self.bottom_frame_text = WebElement(
            self.page.frame_locator("frame[name='frame-bottom']").locator('body'),
            'text of bottom frame',
            page
        )

    def get_text_left_frame(self):
        return self.left_frame_text.get_inner_text()

    def get_text_middle_frame(self):
        return self.middle_frame_text.get_inner_text()

    def get_text_right_frame(self):
        return self.right_frame_text.get_inner_text()

    def get_text_bottom_frame(self):
        return self.bottom_frame_text.get_inner_text()


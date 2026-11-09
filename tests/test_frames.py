from playwright.sync_api import Page
from page_objects.frames_page import FramesPage
from ui.page_actions import PageActions
from logger import setup_logger


logger = setup_logger()


def test_frames_page(page):
    frames_page = FramesPage(page)
    page_actions = PageActions(page)
    url = 'https://the-internet.herokuapp.com/nested_frames'
    left_frame_text = 'LEFT'
    right_frame_text = 'RIGHT'
    bottom_frame_text = 'BOTTOM'
    middle_frame_text = 'MIDDLE'

    page_actions.open_page(url)
    actual_text_left_frame = frames_page.get_text_left_frame()
    assert actual_text_left_frame == left_frame_text, \
        (
            f'Actual: {actual_text_left_frame}\n'
            f'Expected: {left_frame_text}'
        )

    actual_text_right_frame = frames_page.get_text_right_frame()
    assert actual_text_right_frame == right_frame_text, \
        (
            f'Actual: {actual_text_right_frame}\n'
            f'Expected: {right_frame_text}'
        )

    actual_text_bottom_frame = frames_page.get_text_bottom_frame()
    assert actual_text_bottom_frame == bottom_frame_text, \
        (
            f'Actual: {actual_text_bottom_frame}\n'
            f'Expected: {bottom_frame_text}'
        )

    actual_text_middle_frame = frames_page.get_text_middle_frame()
    assert actual_text_middle_frame == middle_frame_text, \
        (
            f'Actual: {actual_text_middle_frame}\n'
            f'Expected: {middle_frame_text}'
        )
from page_objects.hovers_page import HoversPage
from ui.page_actions import PageActions


def test_hovers(page):
    hovers_page = HoversPage(page)
    page_actions = PageActions(page)
    url = 'https://the-internet.herokuapp.com/hovers'

    page_actions.open_page(url)
    number_of_users = hovers_page.count_users()
    for user_index in range(number_of_users):
        expected_user_text = f'name: user{user_index + 1}'
        hovers_page.hover_cursor(user_index)
        actual_user_text = hovers_page.get_name_of_user(user_index)
        assert actual_user_text == expected_user_text, \
            (
                f'Actual: {actual_user_text}\n'
                f'Expected: {expected_user_text}'
            )
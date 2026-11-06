import pytest

from logger import setup_logger
from page_factory import PageFactory


@pytest.fixture(scope='session', autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture
def context(browser, request):
    param = getattr(request, 'param', None)
    page_factory = PageFactory(browser)
    if param is None:
        return browser.new_context()
    else:
        login, password = param
        return page_factory.create_context(login, password)


@pytest.fixture
def page(browser, context):
    page_factory = PageFactory(browser)
    return page_factory.create_page(context)
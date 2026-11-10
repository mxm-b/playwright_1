import pytest
import tempfile
from pathlib import Path
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


@pytest.fixture
def upload_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / 'test_upload.txt'
        file_path.write_text('test file for upload', encoding='utf-8')
        yield file_path
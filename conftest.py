import pytest

from selene import browser


@pytest.fixture(scope='function')
def setting_browser():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 1024
    browser.config.window_width = 1280

    yield

    browser.quit()


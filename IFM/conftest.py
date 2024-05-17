import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nQuit browser...")
    browser.quit()

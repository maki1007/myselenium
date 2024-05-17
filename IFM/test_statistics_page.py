from .pages.login_page import LoginPage
from .pages.login_page import StatisticsPage
import pytest
import time

class TestOnStatisticsPage():
    def test_filters_on_statistics_page(self, browser):
        link = "http://45.12.236.43/login"
        page = LoginPage(browser, link)
        page.open()
        browser.refresh()
        page.authentication()
        page = StatisticsPage(browser, link)
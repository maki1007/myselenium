from .pages.login_page import LoginPage
import time

def test_wrong_alert_of_authentication(browser):
    link = "http://45.12.236.43/login"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(10)
    page.wrong_alert_of_authentication()
def test_login_authentication(browser):
    link = "http://45.12.236.43/login"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(10)
    page.authentication()
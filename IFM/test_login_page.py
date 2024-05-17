from .pages.login_page import LoginPage

def test_wrong_alert_of_authentication(browser):
    global page
    try:
        link = "http://45.12.236.43/login"
        page = LoginPage(browser, link)
        page.open()
        page.wrong_alert_of_authentication()
    except:
        browser.refresh()
        page.wrong_alert_of_authentication()


def test_login_authentication(browser):
    global page
    try:
        link = "http://45.12.236.43/login"
        page = LoginPage(browser, link)
        page.open()
        page.authentication()
    except:
        browser.refresh()
        page.authentication()

def test_not_logging_out_checkbox(browser):
    global page
    try:
        link = "http://45.12.236.43/login"
        page = LoginPage(browser, link)
        page.open()
        page.not_logging_out_checkbox()
    except:
        browser.refresh()
        page.not_logging_out_checkbox()
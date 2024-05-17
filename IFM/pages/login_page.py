from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def wrong_alert_of_authentication(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.send_keys('123')
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys('123')
        confirmation_code = self.browser.find_element(*LoginPageLocators.CONFIRMATION_CODE)
        confirmation_code.send_keys('123')
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        assert self.is_element_present(*LoginPageLocators.WRONG_MESSAGE)
    def authentication(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.send_keys('admin')
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys('testcrm2023')
        confirmation_code = self.browser.find_element(*LoginPageLocators.CONFIRMATION_CODE)
        confirmation_code.send_keys('1111')
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
    def not_logging_out_checkbox(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.send_keys('admin')
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys('testcrm2023')
        confirmation_code = self.browser.find_element(*LoginPageLocators.CONFIRMATION_CODE)
        confirmation_code.send_keys('1111')
        checkbox_not_logging_out = self.browser.find_element(*LoginPageLocators.CHECKBOX_NOT_LOGGING_OUT)
        checkbox_not_logging_out.click()
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

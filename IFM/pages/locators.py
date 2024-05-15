from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "input[id='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    CONFIRMATION_CODE = (By.CSS_SELECTOR, "input[id='code']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    WRONG_MESSAGE = (By.CSS_SELECTOR, "div[class='ant-alert-message']")


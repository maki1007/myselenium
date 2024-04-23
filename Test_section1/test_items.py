from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(10)
    assert len(add_to_cart_button) > 0, "Add to cart button is not found"
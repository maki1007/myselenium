from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element(By.ID, "book")
button.click()

# Находим элемент с значением переменной x
x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)

    # Считаем математическую функцию от x
result = math.log(abs(12*math.sin(x)))

    # Находим поле ввода
answer_input = browser.find_element(By.ID, "answer")
    # Вводим ответ в текстовое поле
answer_input.send_keys(str(result))
# Нажимаем на кнопку "Submit"
submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(10)
browser.quit()
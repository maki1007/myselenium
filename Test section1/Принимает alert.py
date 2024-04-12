from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Запускаем веб-драйвер (например, Chrome)
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("http://suninjuly.github.io/alert_accept.html")

    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    confirm = driver.switch_to.alert
    confirm.accept()
# Находим элемент с значением переменной x
    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # Считаем математическую функцию от x
    result = math.log(abs(12*math.sin(x)))

    # Находим поле ввода
    answer_input = driver.find_element(By.ID, "answer")
    # Вводим ответ в текстовое поле
    answer_input.send_keys(str(result))
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # Закрываем браузер после всех действий
    time.sleep(10)
    driver.quit()

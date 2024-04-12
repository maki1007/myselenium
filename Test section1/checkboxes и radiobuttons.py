from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    # Запускаем веб-драйвер (например, Chrome)
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("https://suninjuly.github.io/math.html")

    # Находим элемент с значением переменной x
    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # Считаем математическую функцию от x
    result = math.log(abs(12*math.sin(x)))

    # Находим поле ввода
    answer_input = driver.find_element(By.ID, "answer")
    # Вводим ответ в текстовое поле
    answer_input.send_keys(str(result))

    # Отмечаем чекбокс "I'm the robot"
    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем радиокнопку "Robots rule!"
    radiobutton = driver.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем на кнопку "Submit"
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Закрываем браузер после всех действий
    time.sleep(10)
    driver.quit()

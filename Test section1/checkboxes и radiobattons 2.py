from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    # Запускаем веб-драйвер (например, Chrome)
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("http://suninjuly.github.io/get_attribute.html")

    # Находим элемент-картинку с сундуком с сокровищами
    treasure_chest = driver.find_element(By.ID, "treasure")

    # Получаем значение атрибута valuex (значение x для задачи)
    x = int(treasure_chest.get_attribute("valuex"))

    # Считаем математическую функцию от x
    result = math.log(abs(12 * math.sin(x)))

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
    time.sleep(30)

    browser.quit()
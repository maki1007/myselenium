from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Запускаем веб-драйвер (например, Chrome)
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("https://suninjuly.github.io/selects1.html")

    # Находим элементы с числами
    num1_element = driver.find_element(By.ID,"num1")
    num2_element = driver.find_element(By.ID,"num2")

    # Получаем значения чисел
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # Считаем сумму чисел
    summa = num1 + num2

    # Находим выпадающий список
    select = Select(driver.find_element(By.TAG_NAME,"select"))
    # Выбираем значение равное расчитанной сумме
    select.select_by_value(str(summa))

    # Нажимаем на кнопку "Submit"
    submit_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
    submit_button.click()

finally:
    # Закрываем браузер после всех действий
    time.sleep(30)
    browser.quit()
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', [
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])


def test_feedback_correct(browser, url):
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.ID, "ember453").click()
    browser.find_element(By.NAME, "login").send_keys("mackarchenko@yandex.ru")
    browser.find_element(By.NAME, "password").send_keys("11111ййййй")
    browser.find_element(By.XPATH, "//button[@class='sign-form__btn button_with-loader ']").click()
    time.sleep(10)
    answer = str(math.log(int(time.time())))
    textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
    textarea.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text
    assert feedback == "Correct!", f"Expected 'Correct!', but got '{feedback}'"
    time.sleep(20)
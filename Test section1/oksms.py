# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Oksms(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_01(self):
        driver = self.driver
        driver.get("https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose")
        driver.find_element(By.ID, "field_email").click()
        driver.find_element(By.ID, "field_email").clear()
        driver.find_element(By.ID, "field_email").send_keys("maki100786")
        driver.find_element(By.ID, "field_password").click()
        driver.find_element(By.ID, "field_password").clear()
        driver.find_element(By.ID, "field_password").send_keys("11111qqqqq")
        driver.find_element(By.XPATH, u"//input[@value='Войти в Одноклассники']").click()
        driver.get("https://ok.ru/?just-logged-in=true")
        driver.get("https://ok.ru/")
        driver.find_element(By.XPATH,"//button[@id='msg_toolbar_button']/span").click()
        driver.find_element(By.XPATH,"//div[@id='msg_layer']").click()
        driver.find_element(By.XPATH, "//msg-chats-list-message[@type='']").click()
        driver.find_element(By.XPATH, "//*[@placeholder='Напишите сообщение...']").send_keys("Тестовое сообщениеcd,.")
        driver.find_element(By.XPATH, "//*[@placeholder='Напишите сообщение...']").submit()
        driver.find_element(By.XPATH, "//*[@class='toolbar-layer_controls_item js-close-layer']").click()
        driver.find_element(By.XPATH,
                            u"(.//*[normalize-space(text()) and normalize-space(.)='Искать на сайте'])[1]/following::*[name()='svg'][3]").click()
        driver.find_element(By.LINK_TEXT, u"Выйти").click()
        driver.find_element(By.ID, "hook_FormButton_logoff.confirm_not_decorate").click()
        driver.find_element(By.ID, "field_email").clear()
        driver.find_element(By.ID, "field_email").send_keys("maki100786")
        driver.find_element(By.ID, "field_password").clear()
        driver.find_element(By.ID, "field_password").send_keys("11111qqqqq")


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

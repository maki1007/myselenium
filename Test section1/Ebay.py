# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Ebay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_01(self):
        driver = self.driver
        driver.get("https://www.ebay.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "gh-ac").send_keys("iphone")
        driver.find_element(By.ID, "gh-btn").click()
        driver.find_element(By.XPATH, "//li[@id='item4485e9c76e']").click()


if __name__ == "__main__":
    unittest.main()
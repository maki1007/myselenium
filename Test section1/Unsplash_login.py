# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Unsplash(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_01(self):
        driver = self.driver
        driver.get("https://unsplash.com/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.NAME, "email").send_keys("powert@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("123456789")
        driver.find_element(By.XPATH, "//button[@value='Login']").click()
        driver.find_element(By.XPATH, "//button[@class='R2LCg p1cWU KHq0c jpBZ0 AYOsT dEcXu xaKx3']").click()
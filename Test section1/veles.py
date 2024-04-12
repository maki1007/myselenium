from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re

class veles(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.edge.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_01(self):
        driver = self.driver
        driver.get("https://test-stdo.velesstroy.com/cp")
        driver.maximize_window()
        driver.find_element(By.ID, "LoginUsername").send_keys("login1")
        driver.find_element(By.ID, "LoginPassword").send_keys("1")
        driver.find_element(By.NAME, "DynamicBrandingLoginEx_loginButton_0").click()
        

import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
    LOGGED_URL = "https://practicetestautomation.com/logged-in-successfully/"
    USERNAME = 'student'
    PASSWORD = 'Password123'

    def test_login_success(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(self.LOGIN_URL)
        time.sleep(5)
        ## Locators
        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.ID, "password")
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

        ## Login
        username_locator.send_keys(self.USERNAME)
        password_locator.send_keys(self.PASSWORD)
        submit_button_locator.click()

        ## logger page locators
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")

        ## Verifications
        actual_url = driver.current_url
        actual_text = text_locator.text

        self.assertEqual(actual_url, self.LOGGED_URL, "correct url for loged")
        self.assertEqual(actual_text, "Logged In Successfully")
        self.assertTrue(logout_button_locator.is_displayed())
        driver.close()

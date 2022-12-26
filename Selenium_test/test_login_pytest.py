import time
import pytest
from selenium.webdriver.common.by import By


class TestLogin:

    LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
    LOGGED_URL = "https://practicetestautomation.com/logged-in-successfully/"
    USERNAME = 'student'
    PASSWORD = 'Password123'

    @pytest.mark.login
    @pytest.mark.positive
    def test_login_success(self,driver):

        driver.maximize_window()

        driver.get(self.LOGIN_URL)
        time.sleep(2)
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

        assert actual_url == self.LOGGED_URL
        assert actual_text == "Logged In Successfully"
        assert logout_button_locator.is_displayed()
        driver.close()

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_login_failed(self, driver, username, password, expected_error_message):
        driver.maximize_window()

        driver.get(self.LOGIN_URL)
        time.sleep(2)
        ## Locators
        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.ID, "password")
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

        ## Login
        username_locator.send_keys(username)
        password_locator.send_keys(password)
        submit_button_locator.click()
        time.sleep(2)

        # Validations
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message
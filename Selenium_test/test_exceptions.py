import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:
    EXCEPTION_PAGE = "https://practicetestautomation.com/practice-test-exceptions/"

    @pytest.mark.exceptions
    def test_no_such_element(self, driver):
        driver.get(self.EXCEPTION_PAGE)
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver,10)
        locator = (By.XPATH, "//div[@id='row2']/input")
        wait.until(ec.presence_of_element_located(locator))

        row_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_input_locator.is_displayed()

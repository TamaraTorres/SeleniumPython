import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

## Locators
username_locator = driver.find_element(By.ID, "username")
password_locator = driver.find_element(By.ID, "password")
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")


## Login
username_locator.send_keys("student")
password_locator.send_keys("Password123")
submit_button_locator.click()

## logger page locators
text_locator = driver.find_element(By.TAG_NAME, "h1")
logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")

## Verifications
actual_url = driver.current_url
actual_text = text_locator.text

assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
assert actual_text == "Logged In Successfully"
assert logout_button_locator.is_displayed()

driver.close()
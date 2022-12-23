from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")

search = driver.find_element(by=By.NAME, value = "q")
search.send_keys("hey, arnold!")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()

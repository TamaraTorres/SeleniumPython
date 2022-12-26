import pytest
import selenium.webdriver.chrome.options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    firefox_options = selenium.webdriver.firefox.options.Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-dev-shm-usage')

    chrome_options = selenium.webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    elif browser == "firefox":
        my_driver = webdriver.Firefox(options=firefox_options)
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
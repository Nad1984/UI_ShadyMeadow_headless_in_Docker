import os
# from selenium_driver_updater import DriverUpdater
from ui_test.src.pages.HomePage import ShadyMeadowsHomePage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


@pytest.fixture(scope="class")
def init_driver(request):

    global driver
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']
    browser = os.environ.get('BROWSER', None)
    # browser = 'chrome'
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception("Provided browser is not one of the supported."
                        f"Supported are: {supported_browsers}.")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('headlessfirefox'):
        firefox_options = FFOptions()
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--headless')
        driver = webdriver.Chrome(options=firefox_options)

    #     setting a class variable
    driver.maximize_window()
    request.cls.driver = driver
    yield ShadyMeadowsHomePage(driver)
    driver.quit()



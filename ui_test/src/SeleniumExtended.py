import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15
        self.__action = ActionChains(self.driver)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def find_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_all_elements_are_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text))

    def click_hold_and_move(self, from_locator, to_locator, timeout=None):
        # WebElement fromElement = driver.findElement(By Locator of fromElement);
        timeout = timeout if timeout else self.default_timeout
        from_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(from_locator)
        )
        to_elements = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(to_locator)
        )
        to_element = to_elements[11]
        # return self.__action.drag_and_drop(from_element, to_element).perform()

        self.__action.move_to_element(from_element).click_and_hold(from_element).perform()
        time.sleep(2)
        self.__action.move_to_element_with_offset(to_element, 10, 0).perform()
        time.sleep(2)
        self.__action.release(to_element).perform()
        return self

        # self.__action.click_and_hold(from_element).perform()
        # return self. driver.execute_script("arguments[0].scrollIntoView(true);", to_element)
        # self.driver.execute_script("document.getElementById('myelementid').scrollIntoView();")

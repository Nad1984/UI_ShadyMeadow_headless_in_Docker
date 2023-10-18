from selenium.webdriver import ActionChains

from ui_test.src.pages.locators.base_page_locators import BasePageLocators
from ui_test.src.helpers.config_helpers import get_base_url
from ui_test.src.SeleniumExtended import SeleniumExtended

import logging as logger


class Feedback(BasePageLocators):
    def __init__(self, selenium):
        self.sl = selenium

    def set_name(self, text):
        logger.info(f"Input name into contact block.")
        return self.sl.wait_and_input_text(self.CONTACT_BLOCK_PERSONS_NAME, text)

    def set_email(self, email):
        logger.info(f"Input email into contact block.")
        return self.sl.wait_and_input_text(self.CONTACT_BLOCK_EMAIL, email)

    def set_phone(self, phone_num):
        logger.info(f"Input phone number into contact block.")
        return self.sl.wait_and_input_text(self.CONTACT_BLOCK_PHONE, phone_num)

    def set_subject(self, subject):
        logger.info(f"Input subject info into contact block.")
        return self.sl.wait_and_input_text(self.CONTACT_BLOCK_SUBJECT, subject)

    def set_message(self, message):
        logger.info(f"Input message into contact block.")
        return self.sl.wait_and_input_text(self.CONTACT_BLOCK_MESSAGE, message)

    def click_submit_button(self):
        logger.info(f"Click SUBMIT button into contact block.")
        return self.sl.wait_and_click(self.CONTACT_BLOCK_SUBMIT_BUTTON)

    def wait_for_message(self, text):
        logger.info("Wait for confirmation message")
        return self.sl.wait_until_element_contains_text(self.MESSAGE, text)

    def wait_for_error_message(self, text):
        logger.info("Wait for confirmation message")
        return self.sl.wait_until_element_contains_text(self.VALIDATE_ERROR_MESSAGE, text)


class ShadyMeadowsHomePage(BasePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.__action = ActionChains(self.driver)
        self.feedback = Feedback(self.sl)

    def go_to_home_page(self):
        base_url = get_base_url()
        logger.info(f"Going to: {base_url}")
        return self.driver.get(base_url)

    def set_window_size(self, width, height):
        return self.driver.set_window_size(width, height)

    def click_on_let_me_hack_button(self):
        button = self.sl.find_element(self.LET_ME_HACK_BUTTON)
        if button:
            logger.debug("Click on 'Let me hack' button")
            return self.sl.wait_and_click(self.LET_ME_HACK_BUTTON)
        else:
            print("No let me hack button")

    def get_logo_picture_element(self):
        logger.debug("Search for LOGO picture.")
        element = self.sl.wait_element_is_visible(self.HOTEL_LOGO)
        return element

    def find_book_single_bedroom_button(self):
        logger.debug("Search for 'Book_this_room_button'.")
        elements = self.sl.find_elements(self.BOOK_THIS_ROOM_BUTTON)
        element = elements[0]
        return element

    def click_book_this_room_button(self):
        logger.debug("Click 'Book_this_room_button'.")
        return self.find_book_single_bedroom_button().click()

    def find_next_bthn(self):
        logger.debug("Find 'Next' button.")
        return self.sl.find_element(self.NEXT_BUTTON)

    def click_next_button(self):
        logger.debug("Click 'Next' button.")
        self.sl.wait_and_click(self.NEXT_BUTTON)

    def go_to_book_button(self):
        book_button = self.sl.wait_element_is_visible(self.BOOK_BUTTON)
        logger.info(f"Move to contact_block 'Book_button'.")
        return self.__action.move_to_element(book_button).perform()

    def select_date(self):
        logger.debug("Choose dates.")
        self.sl.click_hold_and_move(self.FIRST_DATE, self.SECOND_DATE)

    def go_to_contact_block_submit_button(self):
        submit_button = self.sl.find_element(self.CONTACT_BLOCK_SUBMIT_BUTTON)
        logger.info(f"Move to contact_block 'Submit_button'.")
        return self.__action.move_to_element(submit_button).perform()






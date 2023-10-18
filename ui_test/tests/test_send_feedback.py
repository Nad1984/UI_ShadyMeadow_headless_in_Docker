import time
from time import sleep

import pytest
from selenium.common import StaleElementReferenceException
from ui_test.src.pages.HomePage import ShadyMeadowsHomePage
from ui_test.test_data.send_feedback_data import success_send_email_data


@pytest.mark.usefixtures("init_driver")
class TestSendEmail:

    @pytest.mark.tcid3
    @pytest.mark.parametrize("name, email, ph_num, subj, message", success_send_email_data)
    def test_sending_message_successfully(self, name, email, ph_num, subj, message):
        self.print_test_description("TEST send Message!")
        home_page = ShadyMeadowsHomePage(self.driver)
        home_page.go_to_home_page()
        home_page.go_to_contact_block_submit_button()
        home_page.feedback.set_name(name)
        home_page.feedback.set_email(email)
        home_page.feedback.set_phone(ph_num)
        home_page.feedback.set_subject(subj)
        home_page.feedback.set_message(message)
        home_page.feedback.click_submit_button()
        expected_text = f'Thanks for getting in touch {name}'
        home_page.feedback.wait_for_message(expected_text)

    @pytest.mark.tcid4
    # @pytest.mark.parametrize("name, email, ph_num, subj, message", success_send_email_data)
    def test_sending_message_without_name_fails(self):
        self.print_test_description("TEST send Message!")
        home_page = ShadyMeadowsHomePage(self.driver)
        home_page.go_to_home_page()
        home_page.go_to_contact_block_submit_button()
        home_page.feedback.set_email('email@gmail.com')
        home_page.feedback.set_phone('09876543213')
        home_page.feedback.set_subject('subj8459')
        home_page.feedback.set_message('message jeycrienury sljertieojocjrti')
        home_page.feedback.click_submit_button()
        expected_text = f'Name may not be blank'
        home_page.feedback.wait_for_error_message(expected_text)

    def print_test_description(self, description):
        print("***************")
        print(description)
        print("***************")

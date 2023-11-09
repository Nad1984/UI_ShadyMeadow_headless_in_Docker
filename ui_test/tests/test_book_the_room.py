import time
from time import sleep

import pytest
from selenium.common import StaleElementReferenceException

from ui_test.src.pages.HomePage import ShadyMeadowsHomePage
from ui_test.test_data.screen_sizes import mobile_screen_sizes


@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    @pytest.mark.tcid1
    @pytest.mark.parametrize("width, height", mobile_screen_sizes)
    def test_find_logo_picture(self, width, height):
        print("*******")
        print("TEST FIND LOGO")
        print("*******")
        home_page = ShadyMeadowsHomePage(self.driver)
        home_page.set_window_size(width, height)
        home_page.go_to_home_page()
        home_page.click_on_let_me_hack_button()
        picture = home_page.get_logo_picture_element()
        print("PICTURE WAS FOUND")
        print(f"Screen size: {home_page.driver.get_window_size()}")
        print(picture.location)
        assert picture.is_displayed(), f"Logo picture is not displayed"

    @pytest.mark.tcid2
    def test_book_the_room(self):
        print("*******")
        print("TEST E2E")
        home_page = ShadyMeadowsHomePage(self.driver)
        home_page.driver.maximize_window()
        home_page.go_to_home_page()
        book_button = home_page.find_book_single_bedroom_button()
        assert book_button.is_displayed, f"Book_this_room button is not displayed"
        assert book_button.text == 'Book this room'

        home_page.click_book_this_room_button()
        with pytest.raises(StaleElementReferenceException) as e_info:
            # StaleElementReferenceException means the element is no longer in the DOM, or it changed.
            assert book_button.is_displayed(), f"Book_this_room button is displayed, but shouldn't.{e_info}"

        home_page.go_to_book_button()
        # time.sleep(2)
        next_btn = home_page.find_next_bthn()
        assert next_btn.text == 'Next'
        assert next_btn.is_displayed, f"Next button is not displayed"

        home_page.click_next_button()
        # time.sleep(2)
        home_page.select_date()
        # time.sleep(3)

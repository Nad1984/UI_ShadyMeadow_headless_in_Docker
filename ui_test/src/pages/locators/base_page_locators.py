from selenium.webdriver.common.by import By


class BasePageLocators:
    LET_ME_HACK_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    HOTEL_LOGO = (By.CLASS_NAME, 'hotel-logoUrl')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'span.rbc-btn-group:first-child > button:nth-child(3)')
    BOOK_THIS_ROOM_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.float-right.openBooking')
    FIRST_DATE = (By.CSS_SELECTOR, '#root > div:nth-child(2) > div > div:nth-child(4) > div > div:nth-child(2) > div.col-sm-6 > div > div.rbc-month-view > div:nth-child(3) > div.rbc-row-content > div > div:nth-child(4) > button')    # 8 nov
    SECOND_DATE = (By.CSS_SELECTOR, 'button.rbc-button-link') # 11 nov
    ORDER_ROOM_TAB = (By.CSS_SELECTOR, 'div.row.hotel-room-info')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-danger.float-right.book-room')
    BOOK_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.float-right.book-room')
    CALENDAR = (By.CSS_SELECTOR, 'div.rbc-calendar')
    FIRST_NAME = (By.CSS_SELECTOR, 'input.form-control.room-firstname')
    LAST_NAME = (By.CSS_SELECTOR, 'input.form-control.room-lastname')
    EMAIL = (By.CSS_SELECTOR, 'input.form-control.room-email')
    PHONE = (By.CSS_SELECTOR, 'input.form-control.room-phone')
    CONTACT_BLOCK_PERSONS_NAME = (By.CSS_SELECTOR, 'input#name.form-control')
    CONTACT_BLOCK_EMAIL = (By.CSS_SELECTOR, 'input#email.form-control')
    CONTACT_BLOCK_SUBJECT = (By.CSS_SELECTOR, 'input#subject.form-control')
    CONTACT_BLOCK_PHONE = (By.CSS_SELECTOR, 'input#phone.form-control')
    CONTACT_BLOCK_MESSAGE = (By.CSS_SELECTOR, 'textarea#description.form-control')
    CONTACT_BLOCK_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submitContact.btn.btn-outline-primary.float-right')
    MESSAGE = (By.CSS_SELECTOR, '#root > div:nth-child(2) > div > div.row.contact > div:nth-child(2) > div > h2')
    MESSAGE2 = (By.CSS_SELECTOR, '#root > div:nth-child(2) > div > div.row.contact > div:nth-child(2) > div > p:nth-child(2)')
    VALIDATE_ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.alert.alert-danger')

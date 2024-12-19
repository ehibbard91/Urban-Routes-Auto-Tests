from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import helpers
import time

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"taxi")]')
    PLAN_LOCATOR = (By.XPATH, '//img[@src="/static/media/kids.27f92282.svg"]')
    ACTIVE_PLAN_LOCATOR = (By.XPATH, '//img[@src="/static/media/kids.27f92282.svg"]/ancestor::div[contains(@class, "tcard")]')
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, 'np-text')
    PHONE_INPUT_LOCATOR = (By.ID, 'phone')
    FILL_PHONE_NUMBER = (By.CSS_SELECTOR, 'label[class=label]')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button full"]')
    CODE_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#code')
    ENTER_SMS_CODE = (By.CSS_SELECTOR, 'label[class=label]')
    CONFIRM_LOCATOR = (By.XPATH, '//button[contains(text(), "Confirm")]')
    PAYMENT_LOCATOR = (By.CSS_SELECTOR, 'div[class=pp-text]')
    ADD_CARD_LOCATOR = (By.CSS_SELECTOR, 'img[class=pp-plus]')
    ENTER_CC_NUMBER = (By.ID, 'number')
    CVV_NUMBER_LOCATOR = (By.CSS_SELECTOR, 'input#code.card-input')
    LINK_CARD_LOCATOR = (By.XPATH, '//button[contains(text(), "Link")]')
    PAYMENT_ICON_LOCATOR = (By.XPATH, '//img[contains(@src, "card")]')
    COMMENT_LOCATOR = (By.XPATH, '//label[contains(text(), "Message")]')
    COMMENT_INPUT = (By.ID, 'comment')
    TOGGLE_LOCATOR = (By.CSS_SELECTOR, 'span.slider.round')
    CHECKBOX_LOCATOR = (By.CSS_SELECTOR, 'input.switch-input')
    ICECREAM_LOCATOR = (By.CSS_SELECTOR, 'div[class=counter-plus]')
    COUNTER_LOCATOR = (By.CSS_SELECTOR, 'div.counter-value')
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button.smart-button')
    CAR_SEARCH_MODAL_TITLE = (By.CSS_SELECTOR, 'div.order-header-title')


    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        # Enters both 'from' and 'to' fields in one method
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)


    def call_taxi(self):
        taxi_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.TAXI_BUTTON_LOCATOR)
        )
        # Click the "call a taxi" button once it is clickable
        taxi_button.click()

    def select_plan(self):
        # Checks if the option is already selected, if not clicks 'supportive' option
        parent_element = self.driver.find_element(*self.ACTIVE_PLAN_LOCATOR)
        parent_class = parent_element.get_attribute("class")
        if "active" in parent_class:
            pass
        else:
            self.driver.find_element(*self.PLAN_LOCATOR).click()

    def enter_phone(self, phone_number):
        # Locates and clicks phone number
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
        self.driver.implicitly_wait(3)  # Wait up to 3 seconds for popup window to appear
        # Locates phone number input field and enters the phone number
        self.driver.find_element(*self.FILL_PHONE_NUMBER).click()
        phone_input = self.driver.find_element(*self.PHONE_INPUT_LOCATOR)
        phone_input.click()
        phone_input.send_keys(phone_number)
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()
        # Call retrieve_phone_code method from helpers, locates code input field and enters sms code
        sms_code = helpers.retrieve_phone_code(self.driver)
        code_input = self.driver.find_element(*self.CODE_INPUT_LOCATOR)
        code_input.send_keys(sms_code)
        self.driver.find_element(*self.CONFIRM_LOCATOR).click()


    def get_phone_verification(self):
        phone_number_element = self.driver.find_element(*self.PHONE_NUMBER_LOCATOR)
        return phone_number_element.text

    def fill_card(self, cc_number, cvv_number):
        # Fills the cc input fields
        self.driver.find_element(*self.PAYMENT_LOCATOR).click()     # Finds and clicks payment method
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()    # Finds and clicks add card
        # Finds, clicks, and enters cc number
        cc_input = self.driver.find_element(*self.ENTER_CC_NUMBER)
        cc_input.click()
        cc_input.send_keys(cc_number)
        # Finds, clicks, and enters cvv number
        cvv_input = self.driver.find_element(*self.CVV_NUMBER_LOCATOR)
        cvv_input.click()
        cvv_input.send_keys(cvv_number)
        self.driver.find_element(By.TAG_NAME, 'body').click()  # Loses cvv field focus to enable link button
        # Selects link card button
        self.driver.find_element(*self.LINK_CARD_LOCATOR).click()
        # Closes popup window
        self.driver.find_element(By.CSS_SELECTOR, ".payment-picker > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").click()

    def verify_payment(self):
        payment_icon = self.driver.find_element(*self.PAYMENT_ICON_LOCATOR)
        return payment_icon.get_attribute('src') # Will be used to verify cash icon has changed to card

    def add_comment(self, comment):
        input_comment = self.driver.find_element(*self.COMMENT_LOCATOR)
        input_comment.click()
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def verify_comment(self):
        return self.driver.find_element(*self.COMMENT_INPUT).get_attribute("value")

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.TOGGLE_LOCATOR).click()

    def verify_order(self):
        checkbox = self.driver.find_element(*self.CHECKBOX_LOCATOR)
        return checkbox.is_selected()  # This checks if the checkbox is selected

    def order_ice_cream(self, num_ice_creams):
        for i in range(num_ice_creams):   #For loop that will iterate depending on variable
            ice_cream_button = self.driver.find_element(*self.ICECREAM_LOCATOR)
            ice_cream_button.click()
            time.sleep(1)

    def get_counter_value(self):
        counter = self.driver.find_element(*self.COUNTER_LOCATOR)
        return int(counter.text)

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def verify_car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL_TITLE).is_displayed()

    def scroll_page(self, times):
        scrollable_element = self.driver.find_element(By.CSS_SELECTOR, "div.tariff-picker.shown")
        for _ in range(times):
            scrollable_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)





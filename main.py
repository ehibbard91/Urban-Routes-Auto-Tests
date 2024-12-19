
from selenium import webdriver
from data import *      #Imports all constants from data.py
import helpers          #Imports predefined functions from helpers.py
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
    # Tests server response using function from helpers.py file. New servers require data.py url to be updated
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
            exit()
        #Prints message and exits program when not connected to server
            # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(URBAN_ROUTES_URL)

    def test_set_route(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()

    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.enter_phone(PHONE_NUMBER)
        expected_number = urban_routes_page.get_phone_verification()
        assert expected_number == PHONE_NUMBER, f"Expected phone number {PHONE_NUMBER}, but got {expected_number}"

    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.fill_card(CARD_NUMBER, CARD_CODE)  # Fill in the card details
        actual_value = urban_routes_page.verify_payment()  # Call the method to get the 'src' attribute
        expected_value = '/static/media/card.411e0152.svg'  # The expected image path
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.scroll_page(8)    # Scrolls so comment field is visible
        urban_routes_page.add_comment(MESSAGE_FOR_DRIVER)
        actual_value = urban_routes_page.verify_comment()
        assert actual_value == MESSAGE_FOR_DRIVER, f"Expected '{MESSAGE_FOR_DRIVER}', but got '{actual_value}'"

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.scroll_page(8)
        urban_routes_page.order_blanket_and_handkerchiefs()
        # Verification
        actual_value = urban_routes_page.verify_order()
        expected_value = True  # Expecting the checkbox to be selected after the toggle
        # Assert that the checkbox is selected
        assert actual_value == expected_value

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.scroll_page(12)
        num_ice_creams = 2  # Variable for number of ice creams.
        urban_routes_page.order_ice_cream(num_ice_creams)
        # Verify number of ice creams
        actual_value = urban_routes_page.get_counter_value()
        expected_value = num_ice_creams
        assert actual_value == expected_value, f"Expected {expected_value} ice creams, but got {actual_value}"

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.enter_phone(PHONE_NUMBER)
        urban_routes_page.scroll_page(4)
        urban_routes_page.fill_card(CARD_NUMBER, CARD_CODE)
        urban_routes_page.add_comment(MESSAGE_FOR_DRIVER)
        urban_routes_page.scroll_page(4)
        urban_routes_page.order_blanket_and_handkerchiefs()
        urban_routes_page.scroll_page(3)
        urban_routes_page.order_ice_cream(2)
        urban_routes_page.order_taxi()
        actual_value = urban_routes_page.verify_car_search_modal()
        assert actual_value == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

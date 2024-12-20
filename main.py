
from selenium import webdriver
import data      #Imports constants from data.py
import helpers          #Imports predefined functions from helpers.py
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
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


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        # Verify the "From" and "To" fields
        actual_from, actual_to = urban_routes_page.verify_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert actual_from == data.ADDRESS_FROM, f"Expected 'From' address: {data.ADDRESS_FROM}, but got: {actual_from}"
        assert actual_to == data.ADDRESS_TO, f"Expected 'To' address: {data.ADDRESS_TO}, but got: {actual_to}"

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()   # This function is required for the plans to be visible
        urban_routes_page.select_plan()
        assert urban_routes_page.is_plan_active(), "The 'supportive' plan is not active!"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()     # Function required for phone field to be visible
        phone_number = data.PHONE_NUMBER
        urban_routes_page.enter_phone(phone_number)
        assert urban_routes_page.get_phone_verification() == phone_number

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()    # Function required to enter cc info
        urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)  # Fill in the card details
        actual_value = urban_routes_page.verify_payment()
        expected_value = 'card'
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.scroll_page(8)    # Scrolls page to view field
        message = data.MESSAGE_FOR_DRIVER
        urban_routes_page.add_comment(message)
        assert urban_routes_page.verify_comment() == message


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.scroll_page(8)
        urban_routes_page.order_blanket_and_handkerchiefs()
        # Verification
        assert urban_routes_page.get_blanket_and_handkerchiefs__checked() == True   # Verifies that the option is checked


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.scroll_page(12)
        num_ice_creams = 2  # Variable for number of ice creams.
        urban_routes_page.order_ice_cream(num_ice_creams)
        # Verify number of ice creams
        assert urban_routes_page.get_counter_value() == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_plan()
        urban_routes_page.enter_phone(data.PHONE_NUMBER)
        urban_routes_page.scroll_page(4)
        urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_routes_page.add_comment(data.MESSAGE_FOR_DRIVER)
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

import data
import helpers

from data import URBAN_ROUTES_URL
# imports the URBAN_ROUTES_URL constant from data.py file, this will be updated when restarting server
from helpers import is_url_reachable
# imports server check from helpers.py file
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
    # Tests server response using function from helpers.py file. New servers require data.py url to be updated
    def test_set_route(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_select_plan(self):
        # Add in S8
        print('function created for select plan')
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print('function created for fill phone number')
        pass

    def test_fill_card(self):
        # Add in S8
        print('function created for fill card')
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print('function created for comment')
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print('function created for blkt and hndkrchiefs')
        pass

    def test_order_2_ice_creams(self):
        for i in range(2):          #For loop that will iterate twice
            # Add in S8
            print('function created for ice cream')
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print('function created for car search model')
        pass

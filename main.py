import pytest

import data             #Imports constants from data.py
import helpers          #Imports predefined functions from helpers.py

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
        num_ice_creams = 2     #Variable for number of ice creams. Could also be used in data.py
        for i in range(num_ice_creams):   #For loop that will iterate depending on variable above
            # Add in S8
            print('function created for ice cream')
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print('function created for car search model')
        pass

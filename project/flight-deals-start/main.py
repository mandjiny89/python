#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import json

# sheety_endpoint = 'https://api.sheety.co/0b21882be54bbc8da91888790d84dd28/flightDeals/prices'
user_endpoint = "https://api.sheety.co/0b21882be54bbc8da91888790d84dd28/flightDeals/users"
header = {'Authorization': 'Bearer yourbearertoken'}

flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
flight_search_header = {
    'apikey': 'userKey',
    'Content-type': 'application/json'
}

flight_search_parameters = {
    'fly_from': 'LON',
    'fly_to': 'IBZ',
    'date_from': '19/09/2024',
    'date_to': '29/09/2024',
    'return_from': '22/09/2024',
    'return_to': '29/09/2024',
    'adults': '1'
}

# count = 0
# users_list = []
# while count < 2:
#     temp_dict = {}
#     count += 1
#     temp_dict["firstName"] = input("Enter your first name: ")
#     temp_dict["lastName"] = input("Enter your second name: ")
#     temp_dict["email"] = input("Enter your email: ")
#     users_list.append(temp_dict)


# data_manager.request_data(sheety_endpoint, header)
# data_manager.read_data()


flight_search = FlightSearch()
flight_search.search_flight(flight_search_endpoint, flight_search_header, flight_search_parameters)
# flight_search.search_flight()

data_manager = DataManager()
# data_manager.add_users(users_list, user_endpoint, header)
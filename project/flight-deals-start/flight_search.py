import requests
from data_manager import DataManager
from notification_manager import NotificationManager
import json
from pprint import pprint

list_of_cities = DataManager()
email = NotificationManager()

sheety_endpoint_put = "https://api.sheety.co/0b21882be54bbc8da91888790d84dd28/flightDeals/prices/"
header = {'Authorization': 'Bearer userbearertoken'}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def search_flight(self, endpoint, flight_search_header, flight_search_parameters ):
            city_list = list_of_cities.read_data()
            for city in city_list["prices"]:
                flight_search_parameters = {
                    'fly_from': 'LON',
                    'fly_to': city["iataCode"],
                    'date_from': '19/09/2024',
                    'date_to': '29/09/2024',
                    'return_from': '22/09/2024',
                    'return_to': '29/09/2024',
                    'adults': '1'
                }
                try:
                    search_flight_response = requests.get(endpoint, headers=flight_search_header, params=flight_search_parameters)
                    search_results = search_flight_response.json()
                    with open('flight_search_results.json', 'w') as outfile:
                        json.dump(search_results, outfile, ensure_ascii=False, indent=4)
                    # print(search_results)
                    price_list = []
                    for price in search_results["data"]:
                        price_list.append(price["price"])
                    print(f'The lowest price available at the moment from London to {city["city"]} is {min(price_list)}')
                    continue
                except ValueError as e:
                    print(e)
                    print("There is some error let's check ")
                # else:
                #     print(f'The lowest price available at the moment from London to {city["city"]} is {min(price_list)}')

            # if min(price_list) < city["lowestPrice"]:
            #     message = f'Subject: The new cheap price for city from London to {city["city"]} is {min(price_list)}'
            #     email.send_notification(message)

        # with open('flight_search_results.json', 'w') as outfile:
        #     json.dump(search_results, outfile, ensure_ascii=False, indent=4)

        # To read JSON file from local
        # with open('./flight_search_result.json') as f:
        #     search_results = json.load(f)
        # # search_results = json.dumps(data, ensure_ascii=False, indent=4)
        # # print(search_results["data"])
        #

    # def populate_iata_code(self):
    #     search_flight_response = requests.get(endpoint, headers=flight_search_header, params=flight_search_parameters)
    #     search_results = search_flight_response.json()
    #     iata_code = list_of_cities.read_data()
    #     for city_code in iata_code['prices']:
    #         pprint(city_code[''])






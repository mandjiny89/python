import requests
import json
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet

    def request_data(self, endpoint, header):
        sheety_response = requests.get(endpoint, headers=header)
        result = sheety_response.json()
        return result
        # with open('flight_data.json', 'w') as outfile:
        #     json.dump(result, outfile)

    def read_data(self):
        with open('./flight_data.json') as f:
            country_to_visit = json.load(f)
        return country_to_visit

    def update_data(self):
        sheety_response = requests.put(endpoint, headers=header)

    def add_users(self, users_list, user_endpoint, header):
        for user in users_list:
            final_list = {'user': user}
            print(final_list)
            sheety_response = requests.post(user_endpoint, headers=header, json=final_list)
            # sheety_response = requests.get(user_endpoint, headers=header)
            pprint(sheety_response.json())







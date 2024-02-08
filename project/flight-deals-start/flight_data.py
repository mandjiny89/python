class FlightData:
    #This class is responsible for structuring the flight data.
    pass
    # def __init__(self):
    #     pass
    #
    # def manage_flight_data(self):
    #     flight_search_header = {
    #         'apikey': 'apikey',
    #         'Content-type': 'application/json'
    #     }
    #     flight_search_parameters = {
    #         'fly_from': 'LON',
    #         'fly_to': 'IBZ',
    #         'date_from': '19/09/2024',
    #         'date_to': '29/09/2024',
    #         'return_from': '22/09/2024',
    #         'return_to': '29/09/2024',
    #         'adults': '1'
    #     }
    #
    #     {
    #         'price': [
    #             {
    #                 'city': 'Paris',
    #                 'iataCode': 'PAR',
    #                 'lowestPrice': 54,
    #                 'id': 2
    #             },

#ToDo 1. Get the IATA code from each line from googlesheet and check the price for the specific day and compare with current price in the google sheet for the same city.
# ToDo 2. Do this for all the cities in the googlesheet
# ToDo 3. If the price from search is cheaper than the price in googlesheet, send a email alert

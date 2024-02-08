api_key = 'yourKey'

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

import requests

weather_params = {
    "lat": 47.376888,
    "lon": 8.541694,
    "appid": api_key,
    "cnt": 4,
    "list": "list.weather.id"
}

response = requests.get(weather_endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)

weather_data = response.json()
print(weather_data['list'])

will_raining = False

## First setup
# for hourly_data in weather_data['list']:
#     for weather_id in hourly_data['weather']:
#         print(weather_id['id'])
#         if weather_id['id'] < 700:
#             will_raining = True

## simpler Second setup
for hourly_data in weather_data['list']:
    weather_id = hourly_data['weather'][0]['id']
    if int(weather_id) < 700:
        will_raining = True
if will_raining == True:
    print("Bring umbrella")
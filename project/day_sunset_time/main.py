import requests

MY_LONG = "0.759417"
MY_LAT = "52.040623"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

# This will raise any exception if the above request did return apart from 200 status code
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]
print(f"Sunrise: {sunrise} \nsunset: {sunset}")
import time
import requests
import smtplib
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
MY_LAT = 52.040623
MY_LONG = -0.759417

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    #If the ISS is close to my current position
    if MY_LONG-5 <= iss_longitude <= MY_LONG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        # and it is currently dark
        if time_now.hour not in range(sunrise, sunset):
            # Then send me an email to tell me to look up.
            from_email_ID = "sender@gmail.com"
            to_email_ID = "receiver@gmail.com"
            password = "yourpassword"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=from_email_ID, password=password)
                connection.sendmail(
                    from_addr=from_email_ID,
                    to_addrs=to_email_ID,
                    msg=f"Subject: ISS Notification \n\n ISS over your home look up."
                )





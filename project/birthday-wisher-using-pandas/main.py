import pandas as pd
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month

data = pd.read_csv("birthdays.csv")
cleaned_data = data.to_dict(orient="records")


for record in cleaned_data:
    if record['month'] == month and record['day'] == day:
        with open(f"./letter_templates/letter_{random.randint(1,4)}", 'r') as letter:
            custom_letter = letter.read()
        custom_letter = custom_letter.replace("[NAME]", f"{record['name'].title()}")
        from_email_ID = "sender@gmail.com"
        to_email_ID = f"{record['email']}"
        # to_email_ID = "sender@gmail.com"
        password = "yourpass"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_email_ID, password=password)
            connection.sendmail(
                from_addr=from_email_ID,
                to_addrs=to_email_ID,
                msg=f"Subject: Happy Birthday Dear\n\n {custom_letter}."
            )
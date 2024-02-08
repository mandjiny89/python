import datetime as dt
import random
import smtplib


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("./quotes.txt", "r") as quotes:
        lines = quotes.readlines()
    from_email_ID = "sender@gmail.com"
    to_email_ID = "receiver@gmail.com"
    # to_email_ID = "sender@gmail.com"
    # Password comes from the google app password in 2factor verification
    password = "password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email_ID, password=password)
        connection.sendmail(
            from_addr=from_email_ID,
            to_addrs=to_email_ID,
            msg=f"Subject: SMTP Python test\n\n {random.choice(lines)}."
        )

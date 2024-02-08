import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_notification(self, message):
        # Email part SMTP
        from_email_ID = "sender@gmail.com"
        to_email_ID = "receiver@gmail.com"
        password = "password"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_email_ID, password=password)
            connection.sendmail(
                from_addr=from_email_ID,
                to_addrs=to_email_ID,
                msg=f"{message}"
                # msg=f"Subject: Your Stock is {up_or_down} \n\n Headlines is {headline}"
            )

## This block is for sending SMS through TWILIO
# from twilio.rest import Client
#
# TWILIO_SID = YOUR TWILIO ACCOUNT SID
# TWILIO_AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
# TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
# TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER
#
#
# class NotificationManager:
#
#     def __init__(self):
#         self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#
#     def send_sms(self, message):
#         message = self.client.messages.create(
#             body=message,
#             from_=TWILIO_VIRTUAL_NUMBER,
#             to=TWILIO_VERIFIED_NUMBER,
#         )
#         # Prints if successfully sent.
#         print(message.sid)
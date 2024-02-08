import requests
from datetime import datetime, timedelta
from newsapi import NewsApiClient
import smtplib

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

news_url = "https://newsapi.org/v2/everything?q=tesla&searchIn=title,content&from=2024-01-18&to=2024-01-18&language=en&pageSize=3&sortBy=popularity&apiKey=yourkey"
stock_api = "https://www.alphavantage.co/query"

stock_parameters = {
    "symbol" : "TSLA",
    "interval": "60min",
    "function": "TIME_SERIES_DAILY",
    "apikey": "apikey"
}

response = requests.get(stock_api, params=stock_parameters)
stock_data = response.json()

yesterday = str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))
day_before_yesterday = str(datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d'))

## Best way to get the last 2 days of data is to convert the dict to list
# stock_data = response.json().["Time Series (Daily)"]
# data_list = [value for (key, value) in stock_data.items()]
# yesterday_stock_data = data_list[0]
# day_before_yesterday_stock_data = data_list[1]

yesterday_stock_data = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_stock_data = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])

yesterday_close = yesterday_stock_data
day_before_yesterday_close = day_before_yesterday_stock_data

# Test data override commet these two lines when you do realtime data
yesterday_close = 200.88
day_before_yesterday_close = 215.99

up_or_down = round(float((yesterday_close - day_before_yesterday_close)/yesterday_close) * 100)


print(up_or_down)

if up_or_down < 5 and up_or_down > -5:
    print("Not Major Changes in the stock")
else:
    print("Read News")
    response = requests.get(news_url)
    news_data = response.json()
    headline = (news_data['articles'][0]['title']).encode('utf-8').strip()
    print(headline)

    #Email part SMTP
    from_email_ID = "sender@gmail.com"
    to_email_ID = "receiver@gmail.com"
    password = "yourpassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email_ID, password=password)
        connection.sendmail(
            from_addr=from_email_ID,
            to_addrs=to_email_ID,
            msg=f"Subject: Your Stock is {up_or_down} \n\n Headlines is { headline}"
        )

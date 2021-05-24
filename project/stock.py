import requests
import finnhub
import pandas as pd
from datetime import date

# Setup client
finnhub_client = finnhub.Client(api_key="c1chfjf48v6vbcpf1ad0")

# Stock candles
res = finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0)
print(res)

#Convert to Pandas Dataframe
# print(pd.DataFrame(res))


# # help(finnhub_client.stock_candles)


https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=XPEV&interval=60min&apikey=F8Q64V73UOBM1XPX
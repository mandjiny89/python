import requests
import finnhub
import pandas as pd
from datetime import date

# Setup client
finnhub_client = finnhub.Client(api_key="adff")

# Stock candles
res = finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0)
print(res)

#Convert to Pandas Dataframe
# print(pd.DataFrame(res))


# # help(finnhub_client.stock_candles)
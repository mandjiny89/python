import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2021, 4, 1)
end = dt.datetime(2021, 4, 30)

df = web.DataReader('XPEV', 'yahoo', start, end)
print(df.head(30))
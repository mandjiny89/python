import yfinance as yf, pandas as pd, shutil, os, time
from get_all_tickers import get_tickers as gt

# tickers = gt.get_tickers_filtered(mktcap_min=1000000, mktcap_max=10_000_000)
tickers = ["FB", "AMZN", "APPL"]
print("The amount of stocks chosen to observe: " + str(len(tickers)))



shutil.rmtree("/Users/pat/Desktop/vscode/python/project/stock_location/")
os.mkdir("/Users/pat/Desktop/vscode/python/project/stock_location/")

Stock_Failure = 0
Stocks_Not_Imported = 0
Amount_of_API_Calls = 0

i=0
while (i < len(tickers)) and (Amount_of_API_Calls < 1800):
    try:
        stock = tickers[i]  # Gets the current stock ticker
        temp = yf.Ticker(str(stock))  # Instantiate the ticker as a stock with Yahoo Finance
        Hist_data = temp.history(period="max")  # Tells yfinance what kind of data we want about this stock (In this example, all of the historical data)
        Hist_data.to_csv("/Users/pat/Desktop/vscode/python/project/stock_location/stock.csv")  # Saves the historical data in csv format for further processing later
        time.sleep(2)  # Pauses the loop for two seconds so we don't cause issues with Yahoo Finance's backend operations
        Amount_of_API_Calls += 1 
        Stock_Failure = 0
        i += 1  # Iteration to the next ticker
    except ValueError:
        print("Yahoo Finance Back-end Error, Attempting to Fix")  # An error occurred on Yahoo Finance's back-end. We will attempt to retreive the data again
        if Stock_Failure > 5:  # Move on to the next ticker if the current ticker fails more than 5 times
            i+=1
            Stocks_Not_Imported += 1
        Amount_of_API_Calls += 1
        Stock_Failure += 1
print("The amount of stocks we successfully imported: " + str(i - Stocks_Not_Imported))
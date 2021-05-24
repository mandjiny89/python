#DataFlair - Make necessary imports
import quandl
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#DataFlair - Get Amazon stock data
amazon = quandl.get("WIKI/AMZN")
print(amazon.head())
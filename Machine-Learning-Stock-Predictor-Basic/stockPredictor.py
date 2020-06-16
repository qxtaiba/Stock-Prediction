# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uzyyAAPaQujv9K71ae6zm4ESRz4FZUKX
"""

#install dependencies 

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#import stock data

dataFrame = quandl.get("WIKI/FB")
print(dataFrame)

#isolate Adj. Close from dataFrame

dataFrame = dataFrame[["Adj. Close"]]
print(dataFrame)

#variable that will allow you to predict"n" days out into the future

predictOut = 30

dataFrame["Prediction"] = dataFrame[["Adj. Close"]].shift(-30)

print (dataFrame)

#independant data set (X)

#convert dataFrame to numpy array
X = np.array(dataFrame.drop(["Prediction"],1))

#remove the last "n" rows with result NaN
X = X[:-predictOut]

print (X)

#dependent data set (Y)

#convert dataFrame to numpy array
Y = np.array(dataFrame["Prediction"])

#remove the last "n" rows with result NaN
Y = Y[:-predictOut]

print(Y)

#split data into 80% train and 20% test

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

#create and train support vector machine

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#testing model

svm_confidence = svr_rbf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)

#create and train the linear regression  

lr = LinearRegression()
lr.fit(x_train, y_train)

#testing model

lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

#x_forecast equal to the last "n" rows of the original data set from Adj. Close 

x_forecast = np.array(dataFrame.drop(['Prediction'],1))[-predictOut:]
print(x_forecast)

# linear regression model predictions for the next 'n' days

lr_prediction = lr.predict(x_forecast)
print(lr_prediction)

#support vector regressor model predictions for the next 'n' days

svm_prediction = svr_rbf.predict(x_forecast)
print(svm_prediction)
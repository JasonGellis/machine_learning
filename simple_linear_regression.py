# Simple Linear Regression
# reference data_processing_template.py to structure this script

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values # independent variable is 'experience'
y = dataset.iloc[:, -1].values # dependent variable is 'salary'

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature scaling not needed for this exercise

# Fitting the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression # linear regression library
regressor = LinearRegression() # create 'regressor' object from the library

# use .fit method/function from the Linear Regression class - fit the regressor to the training set
regressor.fit(X_train, y_train) 

# the machine is the simple linear regression model is a 'machine' which 
# 'learned' on the training set

# Predicting the Test set results - vector of predictions for the dependent variable
y_pred = regressor.predict(X_test) # use the .predict method to generate predictions
# results - y_pred are the predicted salaries based on the real salaries in y_test

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red') # red are real salary values
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # blue line is predicted values
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red') # red are test set variables
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # vlue line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
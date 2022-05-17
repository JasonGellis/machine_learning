# multiple linear regression
# problem - create a model that tells a company what it should invest in based on profit.
# the company need to understand where (locations) companies perform better, and
# if R&D or marketing generate more profit

#   y    = b0 +   b1     *   x1     +    b2      *     x2     +       b3       *    x3
# profit = b0 + R&D coef (R&D cost) + Admin coef (admin cost) + marketing coef (marketing cost) + 

# Import the libraries
import numpy as np  # math tools
import matplotlib.pyplot as plt  # plotting
import pandas as pd  # import and manage data/datasets

# Importing the dataset
dataset = pd.read_csv('data/50_Startups.csv')
X = dataset.iloc[:, :-1].values # three independent variables
y = dataset.iloc[:, -1].values # last column. Dependent variable

# create dummy variables - as many colums as there are categories (states)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# encoding for independent variable
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3]) # assign numerical values to states
onehotencoder = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder = "passthrough") # passthrough - leave all other columns untouched
X = onehotencoder.fit_transform(X)

# avoiding the Dummy Variable Trap
X = X[:, 1:] # don't take the first column! (Python lm library does this automatically)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

# define 4 variables - X_train, X_test, y_train, y_test - at the same time
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression # linear regression library
regressor = LinearRegression() # create 'regressor' object from the library
regressor.fit(X_train, y_train)

# Predicting the Test set results - vector of predictions for the dependent variable
y_pred = regressor.predict(X_test) # use the .predict method to generate predictions
# results - y_pred are the predicted profits based on the real profits in y_test

# Building an optimal model using Backward Elimination
import statsmodels.api as sm
X = np.append(arr = np.ones((50, 1) ).astype(int), values = X, axis = 1) # add a B0 constant where X0 = 1 (the intercept for OLS)

# create new matrix of features containing the optimal number of statistically significant variables for the model
X_opt = np.array(X[:, [0, 1, 2, 3, 4, 5]], dtype = float)

# 1) SL = 0.05
# 2) Fit model with all possible predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

# 3) Consider the predictor with HIGHEST P-value. If P>SL, go to step 4
regressor_OLS.summary()

# create new matrix of features containing the optimal number of statistically significant variables for the model
X_opt = np.array(X[:, [0, 1, 3, 4, 5]], dtype = float) # X2 is removed (from the original matrix) as it had the highest P-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# create new matrix of features containing the optimal number of statistically significant variables for the model
X_opt = np.array(X[:, [0, 3, 4, 5]], dtype = float) # X1 is removed (from the original matrix) as it had the highest P-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# create new matrix of features containing the optimal number of statistically significant variables for the model
X_opt = np.array(X[:, [0, 3, 5]], dtype = float) # X4 is removed (from the original matrix)  as it had the highest P-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# create new matrix of features containing the optimal number of statistically significant variables for the model
X_opt = np.array(X[:, [0, 3]], dtype = float) # X4 is removed (from the original matrix)  as it had the highest P-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()


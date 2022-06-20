# SVR regression

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the dataset
dataset = pd.read_csv("data/Position_Salaries.csv")

# remove the first column
X = dataset.iloc[:, 1:2].values # matrix of features
y = dataset.iloc[:, 2].values # dependent variable

# splitting data in train and test sets - not needed for this exercise as datas et is too small
# library(caTools)
# set.seed(123)
# split <- caTools::sample.split(dataset$Purchased, SplitRatio = 0.8) # returns 80% TRUE and 20% FALSE
# training_set <- subset(dataset, split == TRUE) # Take TRUE values
# test_set <- subset(dataset, split == FALSE) # Take false values
#
#feature scaling 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(np.array(X).reshape(1, -1))
y = sc_y.fit_transform(y)


# Fit SVR to the dataset
# Create your regressor
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf') # rbf is a non-linear kernel
regressor.fit(X, y)

# Predict new results 
y_pred = regressor.predict(np.array(6.5).reshape(1, -1))

# Visualizing the Regression Model results (for higher resolution and smoother curve)
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
                                       
# Decision Tree Regression (Regression Trees)
# Decision trees are non-continuous. 
# Data Preprocessing Template

# Import the libraries
import numpy as np # maths
import matplotlib.pyplot as plt  # plotting
import pandas as pd  # import and manage data/datasets

# Importing the dataset
dataset = pd.read_csv('../data/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values # independent variable
y = dataset.iloc[:, 2].values # Dependent variable

# create the regressor to fit the Decision Tree to the dataset
from sklearn.tree import DecisionTreeRegressor # import the class
regressor = DecisionTreeRegressor(random_state = 0) # create the object from the class
regressor.fit(X, y) # fit the regressor to the dependent and independent variables

# predicting a new result
y_pred = regressor.predict([[6.5]]) # select for 6.5 specifically using [[]]

# Visualising the decision Tree regression model
# Decision trees are non-continuous, so a "higher resolution" model bust be plotted
X_grid = np.arange(min(X), max(X), 0.01) # increase resolution
X_grid = X_grid.reshape((len(X_grid)), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

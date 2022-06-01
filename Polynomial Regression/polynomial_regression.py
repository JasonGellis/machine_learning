# polynomial regression

# Importing the libraries
import numpy as np  # math tools
import matplotlib.pyplot as plt  # plotting
import pandas as pd  # import and manage data/datasets

# Importing the dataset
dataset = pd.read_csv('data/Position_Salaries.csv')
# even though there is one value for X, by calling a second column you ensure you have a matrix, not a vector.
X = dataset.iloc[:, 1:2].values # independent variable - level
y = dataset.iloc[:, 2].values # last column. Dependent variable

# define 4 variables - X_train, X_test, y_train, y_test - at the same time
# in this case the data set is too small, so we want to train on everything.
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Fitting linear regression to the dataset 
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4) # changing degrees will change the fit of the line. Mess around with it.
X_poly = poly_reg.fit_transform(X) # X_poly column 1 = intercept
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

# Visualising Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1) 
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# predicting a new result with Linear Regression
lin_reg.predict(np.array(6.5).reshape(-1, 1))

# predicitng a new result with polynomial regresson
lin_reg2.predict(poly_reg.fit_transform(np.array(6.5).reshape(-1, 1)))


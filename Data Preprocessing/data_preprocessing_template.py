# Data Preprocessing Template

# Importing the libraries
import numpy as np  # math tools
import matplotlib.pyplot as plt  # plotting
import pandas as pd  # import and manage data/datasets

# Importing the dataset
dataset = pd.read_csv('data/Data.csv')
X = dataset.iloc[:, :-1].values # three independent variables
y = dataset.iloc[:, -1].values # last column. Dependent variable

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

# define 4 variables - X_train, X_test, y_train, y_test - at the same time
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature/variable scaling - salary and age variables are not at same scales and can 
# cause problems with Euclidean distances. 
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

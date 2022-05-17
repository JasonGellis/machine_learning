# Data Preprocessing Template

# Importing the libraries
import numpy as np  # math tools
import matplotlib.pyplot as plt  # plotting
import pandas as pd  # import and manage data/datasets

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # three independent variables
y = dataset.iloc[:, -1].values # last column. Dependent variable

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values= np.nan, strategy='mean')
imputer = imputer.fit(X[:, 1:3]) # select indices 1 & 2. Use 3 because the upper bound is excluded
X[:, 1:3] = SimpleImputer.transform(imputer, X[:, 1:3])

# Dealing with categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # assign numerical values to countries

# because a country can not be represented or compared by a nubmer, we need to 
# create dummy variables - as many colums as there are categories (countries)
onehotencoder = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder = "passthrough")
X = onehotencoder.fit_transform(X)

# encoder for dependent variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

# define 4 variables - X_train, X_test, y_train, y_test - at the same time
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature/variable scaling - salary and age variables are not at same scales and can 
# cause problems with Euclidean distances. 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


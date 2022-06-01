# polynomial regression

# Importing the data set
dataset <- read.csv("data/position_salaries.csv")

# remove the first column
dataset <- dataset[,2:3]

# splitting data in train and test sets - not needed for this exercise as datas et is too small
# library(caTools)
# set.seed(123)
# split <- caTools::sample.split(dataset$Purchased, SplitRatio = 0.8) # returns 80% TRUE and 20% FALSE
# training_set <- subset(dataset, split == TRUE) # Take TRUE values
# test_set <- subset(dataset, split == FALSE) # Take false values
# 
# # feature scaling - need for this either
# training_set[,2:3] <- scale(training_set[,2:3])
# test_set[,2:3] <- scale(test_set[,2:3])

# Fitting the linear regression to the data set
lin_reg <- lm(formula = Salary ~ ., 
              data = dataset)

summary(lin_reg)

# Fitting the Polynomial Regression to the data set

# polynomial regression requires additional independent variables that are 
# polynomial terms of the 1st independent variable. More 'degree' variables help fit the model better
dataset$Level2 <- dataset$Level^2 
dataset$Level3 <- dataset$Level^3 
dataset$Level4 <- dataset$Level^4

poly_reg <- lm(formula = Salary ~ .,
               data = dataset)

summary(poly_reg)

# Visualizing the Linear Regression Results
library(ggplot2)

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), # real observation points
                 colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), # predicted observation points
            colour = 'blue') +
  ggtitle("Truth or Bluff (Linear Regresson)") + 
  xlab('Level') +
  ylab('Salary')
  
# Visualizing the Polynomial Regression Results
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), # real observation points
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), # predicted observation points
            colour = 'blue') +
  ggtitle("Truth or Bluff (Polynomial Regresson)") + 
  xlab('Level') +
  ylab('Salary')

# Predicting a new result with linear regression
# create a new data set to examine a single data point

y_pred <- predict(lin_reg, data.frame(Level = 6.5))

# Predicting a new result with polynomial regression
# create a new data set to examine a single data point

y_pred <- predict(poly_reg, data.frame(Level = 6.5,
                                       Level2 = 6.5^2,
                                       Level3 = 6.5^3,
                                       Level4 = 6.5^4)) # you must input as many values as there are degrees in the poly_reg model



# SVR
library(e1071)

# Importing the data set
dataset <- read.csv("data/position_salaries.csv")

# remove the first column
dataset <- dataset[,2:3]

# splitting data in train and test sets - not needed for this exercise as data s \et is too small
# library(caTools)
# set.seed(123)

# split <- caTools::sample.split(dataset$Purchased, SplitRatio = 0.8) # returns 80% TRUE and 20% FALSE
# training_set <- subset(dataset, split == TRUE) # Take TRUE values
# test_set <- subset(dataset, split == FALSE) # Take false values
# 
# # feature scaling - need for this either
# training_set[,2:3] <- scale(training_set[,2:3])
# test_set[,2:3] <- scale(test_set[,2:3])

# Fitting the Regression  Model to the data set
# Create your regressor
regressor <- svm(formula = Salary ~ .,
                 data = dataset,
                 type = "eps-regression") # be sure to fill out type. Default kernel is Gaussian

# Predicting a new result 
# create a new data set to examine a single data point
y_pred <- predict(regressor, data.frame(Level = 6.5))

# Visualizing the Regression Model results (for higher resolution and smoother curve)
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), # real observation points
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), # predicted observation points
            colour = 'blue') +
  ggtitle("Truth or Bluff (SVR)") + 
  xlab('') +
  ylab('') +
  theme_bw()

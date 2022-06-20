# Decision Tree Regression
library(rpart)
library(ggplot2)

# Data Preprocessing Template

# Importing the dataset
dataset = read.csv("data/position_salaries.csv")
dataset <- dataset[2:3]

# create the regressor
regressor <- rpart(Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1)) # use the rpart minsplit function to for tuning intervals

# Predicting a new result 
y_pred <- predict(regressor, data.frame(Level = 6.5))

# Visualizing the Regression Model results (for higher resolution and smoother curve)
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01) # increase resolution

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), # real observation points
             colour = 'red') +
  geom_line(aes(x = X_grid, y = predict(regressor, newdata = data.frame(Level = X_grid))), # predicted observation points
            colour = 'blue') +
  ggtitle("Truth or Bluff (Decision Tree Regression)") + 
  xlab('Level') +
  ylab('Salary')


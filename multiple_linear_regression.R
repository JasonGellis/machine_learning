# multiple linear regression machine learning model

dataset <- read.csv("data/50_Startups.csv")

# Encoding categorical data
dataset$State <- factor(dataset$State,
                        levels = c("New York", "California", "Florida"),
                        labels = c(1, 2, 3))

# split data set into test and training
library(caTools)
set.seed(123)
split <- caTools::sample.split(dataset$Profit, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Fitting Multiple Linear Regression to the Training set
regressor <- lm(formula = Profit ~ ., # '.' R understands you want to use all variables
                data = training_set) 

summary(regressor)

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

# predicting the Test set results
y_pred <- predict(regressor, newdata = test_set) # vector of predictive results

# build an optimal model using Backward Elimination

# 1) SL = 0.05
# 2) fit model with all variables
regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset) 
summary(regressor)

# 3) eliminate value with highest p-value above SL
regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, # remove state
                data = dataset)
summary(regressor)

regressor <- lm(formula = Profit ~ R.D.Spend + Marketing.Spend, 
                data = dataset) # remove administration
summary(regressor)

regressor <- lm(formula = Profit ~ R.D.Spend,
                data = dataset) # remove marketing and spending
summary(regressor)

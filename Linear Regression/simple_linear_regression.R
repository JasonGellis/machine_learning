# Simple Linear Regression
# use data_processing_template.R to structure this script

# Importing the data set
dataset <- read.csv("data/Salary_Data.csv")

# Split the data into Training and Test data
library(caTools)
set.seed(123)
split <- sample.split(dataset$Salary, SplitRatio = 2/3)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Feature Scaling is not needed

# fit simple linear regression fit to the training_set
regressor <- lm(formula = Salary ~ YearsExperience,
                data = training_set)

# Predicting the test_set results
y_pred <- predict(regressor, newdata = test_set)

# visualize the training set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Salary vs Experience (training set)") +
  xlab("Years of experience") +
  ylab("Salary")
            
# visualize the test set results
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary), # change to test set observations
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), # keep training set line
            colour = "blue") +
  ggtitle("Salary vs Experience (test set)") +
  xlab("Years of experience") +
  ylab("Salary")
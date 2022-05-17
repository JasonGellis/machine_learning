# data preprocessing

# import dataset
dataset <- read.csv("data/Data.csv")
dataset <- dataset[, 2:3]

# splitting data in train and test sets
library(caTools)
set.seed(123)
split <- caTools::sample.split(dataset$Purchased, SplitRatio = 0.8) # returns 80% TRUE and 20% FALSE
training_set <- subset(dataset, split == TRUE) # Take TRUE values
test_set <- subset(dataset, split == FALSE) # Take false values

# feature scaling
# training_set[,2:3] <- scale(training_set[,2:3])
# test_set[,2:3] <- scale(test_set[,2:3])

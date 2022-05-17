# data preproccessing

dataset <- read.csv("data/Data.csv")

# taking care of missing data - Age
dataset$Age <- ifelse(is.na(dataset$Age), # parameter 1: check to see if values are missing
                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), # parameter 2: if true compute the average of the age column
                      dataset$Age) # parameter 3: if parameter 2 is not true, return what is already there

# taking care of missing data - Age
dataset$Age <- ifelse(is.na(dataset$Age), # parameter 1: check to see if values are missing
                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), # parameter 2: if true compute the average of the age column
                      dataset$Age) # parameter 3: if parameter 2 is not true, return what is already there

# Encoding categorical data
dataset$Country <- factor(dataset$Country,
                          levels = c("France", "Spain", "Germany"),
                          labels = c(1, 2, 3))

dataset$Purchased <- factor(dataset$Purchased, 
                            levels = c("No", "Yes"),
                            labels = c(0, 1))

# splitting data in train and test sets
library(caTools)
set.seed(123)
split <- caTools::sample.split(dataset$Purchased, SplitRatio = 0.8) # returns 80% TRUE and 20% FALSE
training_set <- subset(dataset, split == TRUE) # Take TRUE values
test_set <- subset(dataset, split == FALSE) # Take false values

# feature scaling
training_set[,2:3] <- scale(training_set[,2:3])
test_set[,2:3] <- scale(test_set[,2:3])




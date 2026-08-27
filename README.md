# Titanic Survival Prediction

## Project Overview

This project uses the Titanic dataset to build a simple machine learning classification model. The goal is to predict whether a passenger survived or did not survive.

## Data Preparation

Missing values were handled before training the model. Missing `Age` values were replaced with the median age, while missing `Embarked` values were replaced with the most common value. The `Cabin` column was removed because it contained a large number of missing values.

## Feature Engineering

The features used for prediction were `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, and `Embarked`. The categorical features `Sex` and `Embarked` were converted into numerical values using `pd.get_dummies()`.

## Model

A Logistic Regression classification model from scikit-learn was used. The dataset was divided into 80% training data and 20% testing data using `train_test_split()`.

## Evaluation

The model was evaluated using `accuracy_score` and a confusion matrix.

**Final Accuracy: [81.01]%**

## Conclusion

The Logistic Regression model was able to predict passenger survival with reasonable accuracy. The confusion matrix also helped identify correct and incorrect predictions made by the model.

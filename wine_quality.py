import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

colnames = ["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides",
"free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]

'''  1 - fixed acidity
   2 - volatile acidity
   3 - citric acid
   4 - residual sugar
   5 - chlorides
   6 - free sulfur dioxide
   7 - total sulfur dioxide
   8 - density
   9 - pH
   10 - sulphates
   11 - alcohol
   Output variable (based on sensory data):
   12 - quality (score between 0 and 10)'''

red_wine_data = pd.read_csv("data/winequality-red.csv", sep=";")
white_wine_data = pd.read_csv("data/winequality-white.csv", sep=";")

print(red_wine_data.head())
print(white_wine_data.head())


# plt.hist(red_wine_data['quality'], bins = range(1, 11))
# plt.show()

# plt.hist(white_wine_data['quality'], bins = range(1, 11))
# plt.show()

sns.pairplot(red_wine_data)
plt.show()
sns.pairplot(white_wine_data)
plt.show()

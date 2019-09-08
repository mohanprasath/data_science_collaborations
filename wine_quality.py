import pandas as pd
import numpy as np

data = pd.read_csv("data/wine.data")
# names_data = pd.read_csv("data/wine.names")

print(data.head())
# print(names_data.head())

colnames = []
"  1 - fixed acidity
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
   12 - quality (score between 0 and 10)
"

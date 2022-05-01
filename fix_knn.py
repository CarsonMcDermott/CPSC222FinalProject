## this file will fix/write code for the knn


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler      
from sklearn.neighbors import KNeighborsClassifier

## read in file
df = pd.read_csv("shirt_sizes.csv")
print(df)

# kNN algorithm with sci_kit learn library
# notation/convention
# X: a feature matrix (2D data structure where rows are instances and columns are attributes AKA features)
# class column is stroes separately in y
# y: class column (1D data structure)
# AKA class vector, target variable, etc.
# _train and _test in variable names denote out training and testing sets repectively
X_train = df.drop(["t-shirt size"], axis=1)     # to remove the class column
y_train = df["t-shirt size"]
# store x and y train seperately because sci_kit requires it
print(X_train)
print(y_train)
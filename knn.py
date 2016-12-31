import numpy as np
import pandas as pd
import random as rand
import math as m
import matplotlib.pyplot as plt

def dist_from_pt(pt):
    return m.sqrt(((new_point.sepal_length - pt.sepal_length) ** 2) + ((new_point.sepal_width - pt.sepal_width) ** 2))

def knn(k):
    return iris_sorted['species'][0:k].value_counts().index[0]

# Load the data 
iris = pd.read_csv('iris.csv')
iris.head()

# Pick a new point
rand.seed()
new_point = iris.iloc[rand.choice(iris.index.tolist())]

# Sort each point by its distance from the new point, and subset the 10 nearest points
iris['dist_from_pt'] = iris[['sepal_length', 'sepal_width']].apply(func=dist_from_pt, axis=1)
iris.head()

iris_sorted = iris.sort_values(by='dist_from_pt', ascending=True)
iris_k = iris_sorted[0:10]

plt.scatter(iris['sepal_length'],iris['sepal_width'])
plt.scatter(new_point['sepal_length'],new_point['sepal_width'],s=100)
plt.scatter(iris_k['sepal_length'],iris_k['sepal_width'],color='red')
plt.show()

print(knn(10)) 

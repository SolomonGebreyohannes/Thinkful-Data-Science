import numpy as np 
import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as plt 
from sklearn import cross_validation
from sklearn.model_selection import KFold
# from sklearn.cross_validation import train_test_split   

# Load the data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  

kf = KFold(n_splits=10)
for train, test in kf.split(loansData):
    print("%s %s" % (train, test))

# TODO: performance metric 


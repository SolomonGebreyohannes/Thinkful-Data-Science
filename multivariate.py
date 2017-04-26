import pandas as pd
import numpy as np
import statsmodels.api as sm 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Load the Lending Club Statistics 
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

int_rate = [float(value.rstrip('%')) for value in loansData['Interest.Rate']]
annual_inc = loansData['Monthly.Income']
fico = [int(val.split('-')[0]) for val in loansData['FICO.Range']] 
loansData['home_ownership'] = pd.Categorical(loansData['Home.Ownership']).codes
hm_ownshp = loansData['home_ownership'] 
 
# Use income (annual_inc) to model interest rates (int_rate)   
y = np.matrix(int_rate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(annual_inc).transpose()  

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X,missing='drop')
f = model.fit() 
print f.summary()

# Add home ownership (home_ownership) to the model 
x3 = np.matrix(hm_ownshp).transpose()  
x = np.column_stack([x1,x2,x3])

X = sm.add_constant(x)
model = sm.OLS(y,X,missing='drop')
f = model.fit() 
print f.summary() 

import numpy as np
import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as plt 
import math 
 
def logistic_function(coeff, ficoScore, loanAmount): 
	p = [1.0/(1.0 + math.exp(1.0 + (coeff*fc)-(0.000174*loanAmount))) for fc in ficoScore]    
	return p 
   
def pred(p):
	if p>=0.70:
		decision = 1.0  
	else:
		decision = 0.0 
	return decision    

# Load the data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  

# Clean and add columns 
# Drop null rows
loansData.dropna(inplace=True)
# Remove '%' and convert to number  
loansData['Interest.Rate'] = [float(value.rstrip('%')) for value in loansData['Interest.Rate']] 
# FicoScore - split the range and take the first number
loansData['FicoScore'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']] 
# Add IR_TF 
loansData['IR_TF'] = [1 if value >= 12 else 0 for value in loansData['Interest.Rate']]     
# Add ind_vars
loansData['ind_vars'] = 1.0 

# Logistic regression 
logit = sm.Logit(loansData['IR_TF'], loansData['ind_vars'])  
result = logit.fit()
# print result.summary() 
coeff = result.params

loanAmount = 10000
prob = logistic_function(coeff, loansData['FicoScore'], loanAmount)   
# print(coeff)  

plt.plot(loansData['FicoScore'], prob)  
plt.show() 
    

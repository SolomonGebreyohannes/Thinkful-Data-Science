import numpy as np
import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as plt 
import math 
 
def logistic_function(coeff, ficoScore, loanAmount): 
	p = 1.0/(1.0 + math.exp(coeff[0] + (coeff[1]*ficoScore) + (coeff[2]*loanAmount)))
	# p = 1.0/(1.0 + math.exp(-coeff[0] - (coeff[1]*ficoScore) - (coeff[2]*loanAmount)))    
	return p     

def pred(p):  
	if p >= 0.7:
		decision = 1.0
	else:
		decision = 0.0  
	return decision

# Load the data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  

# Clean and add columns 
loansData.dropna(inplace=True)
loansData['Interest.Rate'] = [float(value.rstrip('%')) for value in loansData['Interest.Rate']] 
loansData['FicoScore'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']] 
loansData['IR_TF'] = [1 if value >= 12 else 0 for value in loansData['Interest.Rate']]     
loansData['Intercept'] = 1.0 
ind_vars = ['Intercept', 'FicoScore', 'Amount.Requested']

# Logistic regression 
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])  
result = logit.fit()
coeff = result.params  

# Plot  
loanAmount = 10000
fScore = [ficoScore for ficoScore in range(550,950)]
prob = [logistic_function(coeff,ficoScore,loanAmount) for ficoScore in fScore]
plt.plot(fScore, prob, 'green') 

dec_index = [fs for fs in range(550,950,5)]
dec = [pred(logistic_function(coeff,fs,loanAmount)) for fs in dec_index] 
plt.scatter(dec_index, dec, color='red', s=5) 

plt.show()

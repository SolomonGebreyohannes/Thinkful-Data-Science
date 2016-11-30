import numpy as np
import pandas as pd
import statsmodels.api as sm 

# Load the data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  

# Drop null rows
loansData.dropna(inplace=True) 
 
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']] 
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']] 
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']] 

# Extract columns 
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']  

# Reshape the data 
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose() 
  
# Input matrix 
x = np.column_stack([x1,x2]) 
 
# Model 
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit() 

# Summary  
f.summary() 
 


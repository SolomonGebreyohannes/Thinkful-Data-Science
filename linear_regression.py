import numpy as np
import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as plt 

# Load the data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  

# Clean and extract columns 
# Drop null rows
loansData.dropna(inplace=True)
# Remove '%' and covert to number  
intrate = [float(value.rstrip('%')) for value in loansData['Interest.Rate']]
loanamt = loansData['Amount.Requested']
# Split the range and take the first number
fico = [int(val.split('-')[0]) for val in loansData['FICO.Range']]  

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

# Summary and plot 
print f.summary() 
plt.scatter(fico, intrate, color='red') 
plt.show()

 


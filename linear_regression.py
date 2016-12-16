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
plt.xlabel('FICO Score')   
plt.ylabel('Interest Rate, in %')  
# plt.show() 

plt.hold(True)

fico_score = [1.0*i for i in range(650,800)]  
interest_rate_10 = [73.1137 - (0.0895*fs) + (0.0002*10000.0) for fs in fico_score] 
interest_rate_30 = [73.1137 - (0.0895*fs) + (0.0002*30000.0) for fs in fico_score] 
plt.plot(fico_score, interest_rate_10, 'blue', fico_score, interest_rate_30, 'green') 
plt.show()   

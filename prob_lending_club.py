"""
Challenge

Write a script called "prob_lending_club.py" that reads in the loan data, cleans it, and loads it into a pandas DataFrame. Use the script to generate and save a boxplot, histogram, and QQ-plot for the values in the "Amount.Requested" column. Be able to describe the result and how it compares with the values from the "Amount.Funded.By.Investors".
"""

import matplotlib.pyplot as plt 
import scipy.stats as stats 
import pandas as pd

# Load data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv') 

# Clean data 
loansData.dropna(inplace=True) 

# Plot 
loansData.boxplot(column='Amount.Requested')  
plt.savefig("boxplot_loan.png") 
plt.show()  
  
loansData.hist(column='Amount.Requested', histtype='bar') 
plt.savefig("histogramplot_loan.png") 
plt.show()

fig = plt.figure()
stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)  
plt.savefig("qqplot_loan.png")
plt.show()  
  
fig = plt.figure()
stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)  
stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)  
plt.show()

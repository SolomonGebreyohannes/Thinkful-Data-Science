"""
Write a script called "chi_squared.py" that loads the data, cleans it, 
performs the chi-squared test, and prints the result.
"""

from scipy import stats
import collections 
import pandas as pd 
import matplotlib.pyplot as plt

# Load the data 
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Plot 
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show() 

# Chi-Squared test 
chi, p = stats.chisquare(list(freq.values())) 

# Print 
print chi, p     

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
chi, p = stats.chisquare(freq.values()) 

# Print 
print chi, p     

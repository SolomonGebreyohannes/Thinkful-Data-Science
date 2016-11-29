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
  
loansData.hist(column='Amount.Requested', histtype='bar') 
plt.savefig("histogramplot_loan.png") 

stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)  
plt.savefig("qqplot_loan.png")


import numpy as np
import collections
import scipy.stats as stats 
import matplotlib.pyplot as plt 

# Data  
data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(data)
count_sum = sum(c.values())

# Frequency 
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

# Boxplot  
plt.boxplot(data)
plt.savefig("boxplot.png") 

# Histogram  
plt.hist(data, histtype='bar')
plt.savefig("histogramplot.png") 

## QQ-plot 
stats.probplot(data, dist="norm", plot=plt) 
plt.savefig("qqplot.png")

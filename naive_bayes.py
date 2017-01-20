import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

# Load the data 
aiWeight = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/ideal-weight/ideal_weight.csv')

# Clean data
aiWeight.columns = aiWeight.columns.map(lambda x: (x.replace("'", ''))) 
aiWeight.sex = aiWeight.sex.map(lambda x: (x.replace("'", '')))

# Plot
plt.hist(aiWeight['actual'],bins=20,alpha=0.5, label='Actual')
plt.hist(aiWeight['ideal'],bins=20,alpha=0.5, label='Ideal')
plt.legend(loc='upper right')
plt.show()

aiWeight['diff'].hist(bins=20,color='red')
plt.show()   

# Map "sex" to a categorical variable.
aiWeight['sex'] = aiWeight['sex'].astype('category')

# Are there more women or men in the dataset?
print aiWeight.groupby(['sex']).size()

# Fit Naive Bayes classifier
cl = GaussianNB()
Y = aiWeight.sex
Y = np.array(Y)
X = aiWeight[['actual', 'ideal', 'diff']]
X = np.array(X)
cl.fit(X,Y)

y_pred = cl.fit(X, Y).predict(X)
# print("Number of mislabeled points out of a total %d points : %d"  % (X.shape[0],(Y != y_pred).sum()))
mis = (Y != y_pred).sum()
print "Number of mislabeled: ",mis,"/",X.shape[0]
print "Accuracy = ",float((X.shape[0]-mis)*100)/X.shape[0]
# print("Accuracy was %f percent") % (float(correct * 1000) / X.shape[0])

# Prediction      
print cl.predict([[145, 160, -15]])
print cl.predict(([[160, 145, 15]]))

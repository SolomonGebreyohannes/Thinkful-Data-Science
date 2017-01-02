import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import collections
from scipy.cluster import vq 

# Load the data 
unCountries = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/un/un.csv')

# Determine how many rows are in the dataset. Determine the number of non-null values present in each column. Determine the data type of each column.
for i in unCountries:
    print "Column: ",i,", Number of non-null values: ",len(unCountries[i].dropna()), ", Type: ",  unCountries[i].dtype

# How many countries are present in the dataset? 
print 'Number of countries = ', len(collections.Counter(unCountries['country']))

# Centroid
unCountries = unCountries.dropna()
array = pd.DataFrame.as_matrix(unCountries, columns = ['lifeMale', 'lifeFemale', \
                                'infantMortality', 'GDPperCapita'])
whitened = vq.whiten(array)
centroids = {}
for k in range(1,11):
    centers,dist = vq.kmeans(whitened, k)
    code, distance = vq.vq(whitened, centers)
    distance = np.array(distance).tolist()
    centroids[k] = distance

# Calculate the average within-cluster sum of squares for each centroid. 
for k, v in centroids.iteritems():
    sumsq = 0                          
    for i in v:
        sumsq += i**2
    centroids[k] = round(sumsq / len(v), 1)

# Plot the number of clusters against the average within-cluster sum of squares. At what number of clusters does the curve seem to "level out"?
x_axis = []
y_axis = []
for k, v in centroids.iteritems():
    x_axis.append(k)
    y_axis.append(1000*v)
    
plt.plot(x_axis, y_axis,'-o')
plt.scatter(x_axis[2],y_axis[2],s=100,color='red')
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.show()

# Cluster the UN dataset using k-means clustering with 3 clusters and plot 
centers, dist = vq.kmeans(whitened, 3)
code, distance = vq.vq(whitened, centers)

plt.figure(figsize = (8,6))
plt.scatter(array[code==0][:,3], array[code==0][:,2], c = 'g')
plt.scatter(array[code==1][:,3], array[code==1][:,2], c = 'r')
plt.scatter(array[code==2][:,3], array[code==2][:,2], c = 'b')
plt.xlabel('Per Capita GDP in USD')
plt.ylabel('Infant mortality, per 1000')
plt.show()
 
plt.figure(figsize = (8,6))
plt.scatter(array[code==0][:,3], array[code==0][:,0], c = 'g')
plt.scatter(array[code==1][:,3], array[code==1][:,0], c = 'r')
plt.scatter(array[code==2][:,3], array[code==2][:,0], c = 'b')
plt.xlabel('Per Capita GDP in USD')
plt.ylabel('Male Life Expectancy')
plt.show()

plt.figure(figsize = (8,6))
plt.scatter(array[code==0][:,3], array[code==0][:,1], c = 'g')
plt.scatter(array[code==1][:,3], array[code==1][:,1], c = 'r')
plt.scatter(array[code==2][:,3], array[code==2][:,1], c = 'b')
plt.xlabel('Per Capita GDP in USD')
plt.ylabel('Female Life Expectancy')
plt.show()

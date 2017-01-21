import pandas as pd 
from sklearn import datasets
from sklearn.decomposition import PCA 
from sklearn.lda import LDA 
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from sklearn.lda import LDA
# from sklearn.cross_validation import train_test_split
# from sklearn.neighbors import KNeighborsClassifier

# Load data 
iris = datasets.load_iris()
idata = iris.data 
itarget = iris.target
species = iris.target_names

iris_df = pd.DataFrame(idata, columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
iris_df['Species'] = itarget

# PCA 
pca = PCA(n_components = 2)
reduced_idata = pca.fit_transform(idata) 

# LDA 
lda = LDA(n_components = 2)
reduced_itarget = lda.fit_transform(idata, itarget) 







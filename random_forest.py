import pandas as pd 

# Get data 
subjects = pd.read_csv("UCI HAR Dataset/train/subject_train.txt", header=None, delim_whitespace=True, index_col=False)
subjects.columns = ['Subject']
feature_names = pd.read_csv("UCI HAR Dataset/features.txt", header=None, delim_whitespace=True, index_col=False)
x_vars = pd.read_csv("UCI HAR Dataset/train/X_train.txt", header=None, delim_whitespace=True, index_col=False)

# TODO: random forest  

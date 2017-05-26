# Prediction  

import numpy as np
import pandas as pd 
from sklearn import tree 
import statsmodels.api as sm 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
# from sklearn.feature_selection import SelectFromModel  
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import r2_score  

def get_data(): 

    # source: https://archive.ics.uci.edu/ml/datasets/Facebook+metrics 
    # reference: Moro et al., 2016 
    fb_df = pd.read_csv('dataset_Facebook.csv', sep=';')     
    return fb_df 

def split_data(data): 
    
    train, test = train_test_split(data, test_size = 0.2) 
    return train, test 
	 
def main():
        
    fb_df = get_data() 
    fb_df['Type_ord'] = pd.Categorical(fb_df.Type).codes 
    fb_df = fb_df[['Page total likes','Type_ord','Category','Post Month','Post Weekday','Post Hour','Paid','Lifetime Post Consumers']] 
    
    # print fb_df.isnull().values.any()  # true 
   
    fb_df = fb_df.dropna(axis=0, how='any')
    train, test = split_data(fb_df) 
    
    # print fb_df.isnull().values.any()  # false 

    # train  
    X_train = train[['Page total likes','Type_ord','Category','Post Month','Post Weekday','Post Hour','Paid']] 
    y_train = train[['Lifetime Post Consumers']] 
    # test 
    X_test = test[['Page total likes','Type_ord','Category','Post Month','Post Weekday','Post Hour','Paid']] 
    y_test = test[['Lifetime Post Consumers']] 
    
    # print X_train.isnull().values.any() 

    # 1. model - linear regression   
    X1 = sm.add_constant(X_train) 
    est = sm.OLS(y_train,X1).fit() 

    # y_pred1 = est.predict(X_test) 
    # r21 = r2_score(y_test,y_pred1)    
    # print r21    

    # 2. model - decision trees 
    clf = tree.DecisionTreeClassifier() 
    clf = clf.fit(X_train,y_train) 
    y_pred2 = clf.predict(X_test) 
    r22 = r2_score(y_test,y_pred2)    
    # print r22   
 
    # 3. model - random forest 
    clf = RandomForestClassifier(n_estimators=10) 
    clf = clf.fit(X_train,y_train) 
    y_pred3 = clf.predict(X_test) 
    r23 = r2_score(y_test,y_pred3) 
    # print r23 
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    print "Features sorted by their score:", rf.feature_importances_    
     
if  __name__ =='__main__':main() 







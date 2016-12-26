import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)

train_X, train_y = X[:700], y[:700]
test_X, test_y   = X[700:], y[700:]

train_df = pd.DataFrame({'X': train_X, 'y': train_y})
test_df  = pd.DataFrame({'X': test_X, 'y': test_y})

# Linear and quadratic fit   
poly_1 = smf.ols(formula='y ~ 1 + X', data=train_df).fit()
poly_2 = smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()   

print poly_1.summary()

# Predict   
linear_predict_train = poly_1.predict(train_df['X'])[:700]
quad_predict_train   = poly_2.predict(train_df['X'])[:700]

linear_predict_test = poly_1.predict(test_df['X'])[700:]
quad_predict_test   = poly_2.predict(test_df['X'])[700:]

plt.plot(X,y,train_X,linear_predict_train,train_X,quad_predict_train)
plt.plot(test_X,linear_predict_test,test_X,quad_predict_test)
plt.show()

# Evaluate
mse_linear    = mean_squared_error(train_df['y'], linear_predict_train)
mse_quadratic = mean_squared_error(train_df['y'], quad_predict_train)  












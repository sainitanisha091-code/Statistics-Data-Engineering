import numpy as np 
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3],[ 4], [5]])
Y = np.array([15, 25, 35, 45, 55])
model = LinearRegression()
model.fit(X,Y)
print("slope is ", model.coef_)
print("intercept is ", model.intercept_)
print("pridiction is ", model.predict([[6]]))
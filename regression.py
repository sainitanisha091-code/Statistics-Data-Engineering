import numpy as np 
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([20, 30, 40, 50, 60])
model = LinearRegression()
model.fit(X,Y)
print("slope:" ,model.coef_)
print("intercept" , round(model.intercept_,2))
print("prediction" ,model.predict([[6]]))
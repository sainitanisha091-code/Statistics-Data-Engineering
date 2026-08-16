import numpy as np 
from sklearn.linear_model import LinearRegression
X = np.array([
    [1, 50],
    [2, 60],
    [3, 70],
    [4, 80],
    [5, 90]
])

Y = np.array([30, 40, 50, 60, 70])
model = LinearRegression()
model.fit(X,Y)
model = LinearRegression()  #creates the model
model.fit(X,Y)                #Trains the model
print("slope:" ,model.coef_)    #Gives slope(m)
print("intercept" , round(model.intercept_,2))   #gives intercept(c)
print("prediction" ,model.predict([[60, 100]]))   
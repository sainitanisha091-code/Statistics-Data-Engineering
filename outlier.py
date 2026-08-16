import numpy as np 
Data = np.array([10, 12, 15, 18, 20, 22, 25, 100])
q1 = np.percentile(Data,25)
q3 = np.percentile(Data, 75)
IQR = q3-q1
lower_bound = q1-1.5*(IQR)
upper_bound = q3+1.5*(IQR)
outliers = Data[(Data<lower_bound)| (Data>upper_bound)]
print(q1)
print(q3)
print(IQR)
print(lower_bound)
print(upper_bound)
print(outliers)
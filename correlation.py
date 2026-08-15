import numpy as np 
data1 = np.array([10, 20, 30, 40, 50])
data2 = np.array([15, 25, 35, 45, 55])
correlation = np.corrcoef(data1 , data2)
print(correlation)

import numpy as np 
data = np.array(input().split(), dtype=float)
product = np.prod(data)
geometric_mean = product**(1/len(data))
print(round(geometric_mean,1))
import numpy as np 
values = np.array(input().split(), dtype=float)
weight = np.array(input().split(), dtype=float)
avg = np.average(values, weights=weight)
print(avg)
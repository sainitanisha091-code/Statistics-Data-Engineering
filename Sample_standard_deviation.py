import numpy as np 
sales = np.array(input().split(), dtype= float)
sample_mean = np.mean(sales)
sample_standard_deviation = np.std(sales , ddof=1)
print(sample_mean)
print(sample_standard_deviation)
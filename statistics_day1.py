import numpy as np 
data = np.array([12, 15, 18, 20, 25, 30, 35])

mean = np.mean(data)
print(mean)

median = np.median(data)
print(median)

variance = np.var(data)
print(variance)

standard_deviation = np.std(data)
print(standard_deviation)

range_value = np.max(data)-np.min(data)
print(range_value)

minimum = np.min(data)
print(minimum)

maximum = np.max(data)
print(maximum)

sum = np.sum(data)
print(sum)

length = len(data)
print(length)
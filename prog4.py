import numpy as np 
sales = np.array(input().split(), dtype=float)
maximum = int(np.max(sales))
minimum = int(np.min(sales))
range_value = maximum-minimum
mid_point = (maximum+minimum)/2
print(maximum)
print(minimum)
print(range_value)
print(mid_point)

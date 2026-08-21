import numpy as np 
sales = np.array(input().split(), dtype=float)
mean = np.mean(sales)
std = np.std(sales)
z = np.abs((sales-mean)/std)
values = sales[z<=2]
mean2  = np.mean(values)
print(mean2)


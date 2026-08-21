import numpy as np 
sales = np.array(input().split(), dtype=float)
mean =  np.mean(sales)
std = np.std(sales)

z= np.abs((sales-mean)/std)
unusual = sales[z>2]
print(np.sort(unusual))
print(len(unusual))


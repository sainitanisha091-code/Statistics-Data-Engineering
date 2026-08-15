import numpy as np 
sales = np.array(input().split(), dtype = float)
med = np.median(sales)
count = (sales>med).sum()
print(med)
print(count)
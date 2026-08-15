import numpy as np 
sales = np.array(input().split(), dtype=float)
avg = np.mean(sales)
count = (sales>avg).sum()
print(avg)
print(count)
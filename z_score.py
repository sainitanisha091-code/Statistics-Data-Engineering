import numpy as np 
sales = np.array(input().split(), dtype=float)
mean = np.mean(sales)
standard_deviation = np.std(sales)
z_score = (sales-mean)/standard_deviation
print(z_score)
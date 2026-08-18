import numpy as np 
sales = np.array(input().split(), dtype=float)
population_varience = np.var(sales)
sample_varience = np.var(sales, ddof=1)
print(population_varience)
print(sample_varience)
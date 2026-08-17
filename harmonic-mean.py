import numpy as np 
from scipy.stats import hmean
data = np.array(input().split(), dtype = float)
harmonic = hmean(data)
print(harmonic)
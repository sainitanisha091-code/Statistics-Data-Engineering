import pandas as pd 
Data = pd.Series([5, 10, 15, 20, 100])
skewness = Data.skew()
print(skewness)
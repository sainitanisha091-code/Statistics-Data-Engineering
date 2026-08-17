import pandas as pd 
sales = pd.Series([10, 20, 20, 30, 30, 40])
mode = sales.mode().min()
frequency = (sales==mode).sum()
print(mode)
print(frequency)
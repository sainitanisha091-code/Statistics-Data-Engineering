import pandas as pd 
sales = pd.Series([10, 20, 20, 30, 30, 30, 40])
mode = sales.mode()
frequency = (sales==mode.iloc[0]).sum()
print(mode)
print(frequency)

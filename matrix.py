import numpy as np 

rows = int(input("Enter Rows: "))
cols = int(input("Enter Cols: "))

arr = []

for i in range(rows):
  row = list(map(int, input().split()))
  arr.append(row)

arr = np.array(arr)

print(arr.shape)
print(arr.size)
print(arr[1,2])
print(np.sum(arr, axis = 1))
print(np.sum(arr, axis = 0))

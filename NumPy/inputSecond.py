import numpy as np
row = int(input("Row : "))
col = int(input("Col : "))

arr = np.empty((row,col))

for i in range(row):
    for j in range(col):
        element = float(input("Enter the element at position {} and {} :".format(i,j)))
        arr[i,j]=element

print(arr)













# import numpy as np
# row = int(input("Row : "))
# arr = np.empty(row)
# for i in range(row):
#     element = int(input())
#     arr[i] = element

# print(arr)


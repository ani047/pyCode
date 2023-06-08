import numpy as np
sum=0
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
num = arr.size-1
print(arr)

print(np.sum(arr))
for i in arr:
    print(i)

for m in arr:
    for n in arr[m]:
        print(arr[m,n])
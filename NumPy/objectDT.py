import numpy as np
arr = np.array([1,3,5,7])
print(arr)
for i in arr:
    print(i)

print(arr.dtype)


arr1 = np.array(['A','B','C','D'])
print(arr1)
print(arr1.dtype)

newArr=arr.astype('f')
print(newArr)

arr4 = np.asarray
tuple1 = (1,2,3,4,5)
print(type(tuple1))
print(tuple1)
newTuple = np.array(tuple1)
print(newTuple)
print(newTuple.ndim)
arr5 = [[1,2,3],[3,4,5],[5,6,7]]
print(arr5)
for i in arr5:
    print(i)
print(len(arr5))
nums = np.array([[12,43,56],[2,65,40],[32,42,76],[64,97,65]])

print(nums[0,2])

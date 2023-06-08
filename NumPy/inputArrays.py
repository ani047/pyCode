from array import *
arr = array('i',[])
num = int(input("Enter num:"))
for i in range(num):
    arr.append(int(input()))

print("Space")
for i in range(len(arr)):
    print(arr[i])


import numpy as np
arr = np.array([[1,2,3,4,5],[10,20,30,40,50]])
for x in arr:
    print(x)
    for y in x:
        print(y)

print("3D Array:")
ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for i in ar:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)
    

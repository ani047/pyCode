def arraySory(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr


arr=[[4,3,2],[8,7,4],[9,2,1]]
print(arr) 
for i in range(3):
    arr.append(arraySory(arr[i]))

print(arr)

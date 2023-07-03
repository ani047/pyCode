def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr

rootList=[8,3,4,7,2,1,5,8,4]
print(rootList)
print("Sorted:",bubbleSort(rootList))


#bubble sort algo...
'''for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
return arr'''
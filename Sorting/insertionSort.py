def insertionSort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr


rootArr=[7,3,5,2,8,3,2,6,4]
print(rootArr)
print(insertionSort(rootArr))
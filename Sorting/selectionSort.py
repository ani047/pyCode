def selectionSort(arr,size):
    for i in range(size):
        min_Index = i
        for j in range(min_Index+1,size):
            if(arr[j]<arr[min_Index]):
                min_Index = j
        
        (arr[i],arr[min_Index]) = arr[min_Index],arr[i]


arr = [1,4,2,11,18,3,5,2,9]
print(arr)
length = len(arr)

selectionSort(arr,length)

print(arr)

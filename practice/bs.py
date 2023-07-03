def binarySearch(arr,key):
    length = len(arr)
    s=0
    e=len(arr)-1 
    mid = int(s+(e-s)/2)
    while s<=e:
        if arr[mid] == key:
            return mid
        
        if arr[mid]>key:
            e=mid-1
        else:
            s=mid+1
        mid =int(s+(e-s)/2)
    return 

lst = [2,4,6,7,8,12,34]
print(binarySearch(lst,4))

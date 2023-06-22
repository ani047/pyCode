def highest_product(arr):
    length=(len(arr))
    if length<2:
        print("No such a pair exist in array...")
        return
    a=arr[0]
    b=arr[1]
    for i in range(length):
        for j in range(i+1,length):
            if arr[i]*arr[j]>(a*b):
                a=arr[i]
                b=arr[j]
    return a,b

rootList = eval(input("List:"))
print(highest_product(rootList))
def missingNumber(array,n):
    for i in range(1,n):
        if i not in array:
            return i
    
            
    

n=5
arr=[1, 2, 3, 5]     
print(missingNumber(arr,n))
            
'''num = int(input("Num: "))
lst=[]
for i in range(1,num):
    item = int(input())
    lst.append(item)

lst = sorted(lst)
lst2=[]
for j in range(1,num):
    lst2.append(j)
print(lst)
print(lst2)



for element in range(1,n):
    if lst[element] != lst2[element]:
         print(lst2[element])
         break
'''


s = input("String: ")
num_lst=[]
str_lst=[]
for item in s:
    if item.isalpha():
        str_lst.append(item)
    else:
        num_lst.append(item)
print(str_lst)
print(num_lst)
lst=[]
finalList=[]
for item in num_lst:
    lst.append(int(item))
for i in range(len(lst)):
    finalList.append(str_lst[i]*lst[i])
print(finalList)
print(''.join(finalList))

 

 
    

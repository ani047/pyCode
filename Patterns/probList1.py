# set the 0 at the end of list...
list1 = [1,2,0,2,3,8,0,1,0,2,5]
print(list1)
for item in list1:
    if item == 0:
        list1.remove(item)
        list1.append(item)
print("After setting 0...")
print(list1)
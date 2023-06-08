list = ['main_key','parent_key','Basic_key','right_key']
my_list=[]
for item in list:
    temp = item.replace('_',' ')
    my_list.append(temp)


print(my_list)


list1 = [1,2,3,4,5]
sumy = 0
for i in list1:
    sumy = sumy + i
print("sum is ",sumy)

print(sum(list1))

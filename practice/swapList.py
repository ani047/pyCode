root_List = []
size = int(input("Size:"))
for i in range(size):
    num = int(input("Value for index {} is:".format(i)))
    root_List.append(num)

print(root_List)



s = 0
e = len(root_List)-1
while(s<e):
    root_List[s],root_List[e] = root_List[e],root_List[s]
    s+=1
    e-=1
print("After Swap...")
print(root_List)


root_List = []
size = int(input("Enter the Size:"))
for n in range(size):
    temp_Input = int(input("Value for index {} is: ".format(n)))
    root_List.append(temp_Input)

print(root_List)

# creating new list...
new_List = []

for i in root_List:
    if i%2 != 0:
        new_List.append(i)

for i in root_List:
    if i%2 == 0:
        new_List.append(i)

print()
print(new_List)

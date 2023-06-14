list1 = []
num = int(input("Enter the size:"))
for i in range(num):
    temp_input = int(input("Value for index {} is:".format(i)))
    list1.append(temp_input)
sum = 0
for n in list1:
    sum = sum + n


print(list1)
print(sum)

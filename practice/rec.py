num = int(input("Enter the Value"))
l1 = []

for i in range(1,num+1):
    l1.append(i)

print(type(num))
print(l1)

sum=0
for x in l1:
    sum = sum + x

print(sum)
print(len(l1))

n_tuple = int(input("Enter the Num for Tuple:"))
tuple = ()
for i in range(n_tuple):
    tuple = i

print(tuple)
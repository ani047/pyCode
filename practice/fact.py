num = int(input("Num:"))
fact = 1
for n in range(1,num+1):
    fact = fact * n

print("Factorial of {} is {}".format(num,fact))

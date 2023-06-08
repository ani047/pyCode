n = int(input("Enter Number:"))
temp = n
num = 0
while n>0:
    digit = n%10
    num = num * 10 + digit
    n = n//10

print(num)
print(temp)
if temp==num:
    print("True")
else:
    print("False")
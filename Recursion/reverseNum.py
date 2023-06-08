num = int(input("Enter num:"))
temp = num
def reverse(num):
    if num==0:
        return 1
    digit = num%10
    n = (n*10)+digit
    reverse(num//10)
    return n

if temp==reverse(num):
    print("True")
else:
    print("False")

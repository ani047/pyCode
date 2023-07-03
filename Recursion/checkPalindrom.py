def checkPalindrom(num,ans):
    if num==0:
        return ans 
    dig = num % 10
    ans = ans * 10 + dig
    return checkPalindrom(num // 10,ans)
    



n = int(input("Nums: "))
ans = 0
temp = checkPalindrom(n,ans)
print(temp)
if n == temp:
    print("Palindrom")
else:
    print("Not a Palindrom")
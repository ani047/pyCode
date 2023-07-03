def checkPalindrom(nums):
    ans = 0
    while nums>0:
        dig = nums%10
        ans = ans*10+dig
        nums = nums//10
    return ans

n = int(input("Num:"))
temp =(checkPalindrom(n))
if n==temp:
    print(f"Yes, {n} is a Palndrom")
else:
    print(f"Nope, {n} is not a Palindron")
    
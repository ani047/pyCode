def is_prime(num):
    if num <2:
        return False
    for i in range(2,(num**0.5)+1):
        if num%i==0:
            return False
    return True
num = int(input("nums:"))
primeList = []
for item in range(2,num+1):
    if is_prime(num):
        primeList.append(item)
sum = 20
ans = 0 
for i in primeList:
    if sum==(ans+i):
        print(ans)



def digSum(num,sum):
    if num == 0:
        return sum
    dig = num % 10
    sum = dig+sum
    return digSum(num//10,sum)

n = int(input("Num: "))
sum =0
print(f"the Sum of {n} is {digSum(n,sum)}")

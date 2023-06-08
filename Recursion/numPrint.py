def printing(num):
    if num==0:
        return 0
    printing(num-1)
    print(num)

n = printing(10)
print(n)



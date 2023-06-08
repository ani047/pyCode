num  = int(input("Num:"))
for i in range(num+1):
    for space in range(num-i):
        print(end=' ')
    for j in range(i):
        print("#",end='')
    print()

#line num 6 has space with payramid pattern....

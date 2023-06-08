num = int(input("Num: "))
for i in range(num+1):
    for j in range(i):
        print(end=' ')
    for k in range(num-i):
        print('#',end='')
    print()



# in lne num 6 its has only space and make the pattern reverse payramid
row = 8
col = 4
for i in range(row):
    for j in range(row-i):
       print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

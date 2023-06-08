def func(mylist):
    for i in mylist:
        if i%2==0:
            yield i
mylist = [2,5,3,12,1,7]

for j in func(mylist):
    print(j,end=" ")

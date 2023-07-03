n=int(input("Nums: "))
lst=[]
for i in range(n):
    item = int(input())
    lst.append(item)

print(lst)

dict = dict()
for item in lst:
    if item in dict:
        dict[item]+=1
    else:
        dict[item]=1

print(dict)
for num in dict:
    if dict[num]==1:
        print(num)


print(sorted(dict))

print(dict.get(7))
nums = 0
val = 0
for item in dict:
    if nums<dict.get(item):
        nums = dict.get(item)
        val = dict[item]

print(val," is",nums ,"Times")

        
     
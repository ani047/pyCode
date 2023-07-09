str = input("String:")
lst = []
for i in str:
    if i in ['a','e','i','o','u']:
        lst.append(i)
print(lst)
dict = {}

for ch in lst:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
list1=[]
for j in dict:
    if dict[j]==1:
        list1.append(j)

print("".join(list1))
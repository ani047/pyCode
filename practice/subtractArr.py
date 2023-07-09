lst1 = [7,6,4,3,8,2,3]
lst2 = [2,7,5,4,2,7,9]
len1 = len(lst1)
len2 = len(lst2)

ans1 =""
for num in lst1:
    ans1+=str(num)

ans2 =""
for num in lst2:
    ans2+=str(num)

# subtraction
ans = int(ans1)-int(ans2)
lst = []
while ans>0:
    nums=ans%10
    lst.append(nums)
    ans=ans//10

s=0
e=len(lst)-1
while s<e:
    lst[s],lst[e]=lst[e],lst[s]
    s+=1
    e-=1

print(lst1)
print(lst2)
print(lst)


    
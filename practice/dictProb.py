list = [{"science":[74,98,67,86]},{"English":[75,87,60,78]}]
lst=[]

for i in list:
    temp = (i.values())
    for i in temp:
        lst.append(i)

lst1=lst[0]
lst2=lst[1]
keys=[]
for i in list:
    temp=i.keys()
    for j in temp:
        keys.append(j)
finalList=[]
temp={}
print(keys)

for i in range(len(lst1)):
    for j in range(len(keys)-1):
        temp[keys[j]]=lst1[i]
        finalList.append(temp)
        temp={}
        j+=1
        temp[keys[j]]=lst2[i]
        finalList.append(temp)
        temp={}

print(finalList)
    

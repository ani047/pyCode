str = input()
str = sorted(str)
list1=list()
for ch in str:
    list1.append(ch)

dict = {}
for item in list1:
    if item in dict:
        dict[item]+=1
    else:
        dict[item]=1

charList=list()
for i in dict:
    charList.append(i)
print(charList)

numList=[]
for j in dict:
    numList.append(dict[j])

print(numList)


fnlList=[]
for nums in range(len(numList)):
    fnlList.append(charList[nums])
    fnlList.append(numList[nums])

numList=str(numList)
print(fnlList)
print("".join(fnlList))




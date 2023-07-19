'''keyList = ["name","id"]
valueList=["Gfg",12,"Anil",10]
list=[]
dict={}
num =0
for i in range(len(valueList)):
    while num<2:
        for j in range(len(keyList)-1):
            temp = dict[keyList[j]]=valueList[i]
            list.append(temp)
            i+=1
            temp={}
            j+=1
            temp = dict[keyList[j]]=valueList[i]
            list.append(temp)
            temp={}
        num+=1
print(list)'''
keyList = ["name","id"]
valueList=["Gfg",12,"Anil",10]
list=[]
dict={}
keyLen=0
valueLen =0
num =0
temp={}

for i in range(len(valueList)):
    temp=dict[keyList[i]]=keyList[num]
    list.append(temp)
    num+=1
    if num==2:
        num=0
print(list)
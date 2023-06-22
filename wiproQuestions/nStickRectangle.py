def stickRectangle(nStick,arr):
    newList = []
    for i in arr:
        if arr.count(i)>=2:
            newList.append(i)
    newList =list(set(newList))
    print(newList)
    maxArea = 0
    for i in range(len(newList)):
        for j in range(i+1,len(newList)):
            if newList[i]*newList[j]>maxArea:
                maxArea=newList[i]*newList[j]
    return maxArea


num=int(input("Num: "))
rootList=[]
for i in range(num):
    temp = int(input())
    rootList.append(temp)
finalAns = stickRectangle(num,rootList)
print(finalAns)


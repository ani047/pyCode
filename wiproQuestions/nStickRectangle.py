def stickRectangle(nStick,arr):
    newList = []
    for i in arr:
        if arr.count(i)>=2:
            newList.append(i)
    newList =list(set(newList))
    print(newList)

num=int(input("Num: "))
rootList=[]
for i in range(num):
    temp = int(input())
    rootList.append(temp)
stickRectangle(num,rootList)



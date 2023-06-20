str = input("String:")
nums = int(input("Nums:"))
root_List=str.split()
new_Dict = dict()
for item in root_List:
    if item in new_Dict:
        new_Dict[item]+=1
    else:
        new_Dict[item]=1

new_List = []
for key in new_Dict:
    if new_Dict[key]>=nums:
        new_List.append(key)


if len(new_List)>0:
    print(new_List)
else:
    print("NA")


    
'''#userInput that will be string...
str = input("String: ")

#userInput that will be Nums...
n = int(input("Nums:"))

str = str.split()
new_Dict=dict()
for item in str:
    if item in new_Dict:
        new_Dict[item]=+1
    else:
        new_Dict[item]=1

new_List = []
for key in new_Dict:
    if new_Dict[key]>=n:
        new_List.append(key)

if len(new_List)>0:
    print(new_List)
else:
    print('NA')'''



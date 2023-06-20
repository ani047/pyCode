'''def listToset(root_List):
    root_Set = set(root_List)
    new_List = list(root_Set)
    return new_List

baseList = [1,2,3,3,4,2,4,1,5,9]
print(baseList)
print(listToset(baseList))
'''

original_List = [1,3,1,3,2,4,2]
print(original_List)
set_Data = set(original_List)

original_List = list(set_Data)
print(original_List)
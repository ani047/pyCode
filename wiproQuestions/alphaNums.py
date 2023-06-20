user_Input = input("String: ")
alpha = []
nums = []
for item in user_Input:
    if item.isalpha():
        alpha.append(item)
    else:
        nums.append(item)

ansList = alpha+nums
final_List = ''.join(ansList)
print(final_List)



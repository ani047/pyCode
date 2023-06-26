def equal(n,m,s,t):
    counter=0
    #for spit the char of string...
    splited_list=list()
    for i in s:
        char = splited_list.append(i)
    print(splited_list)
    for item in range(n):
        char = splited_list.pop(item)
        for word in t:
            if "".join(splited_list)==word:
                counter+=1
        splited_list.insert(item,char)
    return counter
arr=['bcde','bcad','bcde','acde']
print(equal(5,4,'abcde',arr))




'''Str='abcde'
lenStr=len(Str)
numsElement=int(input("Size of t:"))
t=[]
print("String size will be {}...".format(lenStr-1))
for i in range(numsElement):
    temp=input()
    t.append(temp)
n=lenStr-1
nums=0
start=0
while n>0:
    for item in t:
        tempStr=Str.split()
        tempStr.remove(tempStr[start])
        newStr="".join(tempStr)
        if newStr==item:
            nums+=1
    start+=1
    n-=1

print(nums)'''

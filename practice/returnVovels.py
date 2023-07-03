Str=input()
Str=Str.lower()
lst = ['a','e','i','o','u']
strList=''
for item in range(0,len(Str)):
    if Str[item] in lst:
        strList+=Str[item]
print(strList)

    
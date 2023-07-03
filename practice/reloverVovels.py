s=input("Strings: ")
s=s.lower()
print(s)
finalS=''
for item in s:
    for ch in item:
        if ch not in ['a','e','i','o','u']:
            finalS+=ch
print(finalS)

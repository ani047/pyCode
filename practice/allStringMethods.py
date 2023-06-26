# 1. capitalize...
str = '''anil meran from cdgi.
you know what? He is very good in study.'''
print(str.capitalize())

# 2. casefold()

str1 = "ANIL FROM CDGI."
print(str1.casefold())

# 3. lover()

print(str1.lower())

# 4. upper()
str2 = 'anil meran from cdgi.'
print(str2.upper())

# 5. swapcase()
string = 'HELLO WORLD.'
print(string.swapcase())

# 6. title()
string2 = 'from the cdgi i came at my home.'
print(string2.title())

# 7. center(width,fillchar)
name = 'Anil Ji'
print(name.center(19,'_'))

# 8. ljust()
print(name.ljust(16))
print(name.ljust(16,'-'))
# 9 rjust()
print(name.rjust(10,'-'))

# 10. zfill()
nums = '345'
print(nums.zfill(5,))

# 11. strip()
string3 = 'hello world'
print(string3.strip("  eh"))

rootStr = 'ErAnil ErMeran baFrom caSunil caMeran' 
rootList = rootStr.split()
print(rootList)
new_List=[]
for item in rootList:
    new_List.append(item[2:])
print(new_List)
newStr = ' '.join(new_List)
print(newStr)
print(newStr.index('Meran',5,12))


sys = "I can do it anything can you belive me"
print(sys.replace("can",'May',1))

print(sys.split(','))

a=" "
print(a.isspace())

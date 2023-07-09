list = [23,7,8,5,13]
item1 =list[0]
for num in list:
    if num >item1:
        item1=num

print(item1)
item2=12344
for num in list:
    if num<item2:
        item2=num
print(item2)

print(item1-item2)

str ='im anil meran from indore'
lst = str.split()
print(lst[::-1])


for ch in range(len(str)):
    str[ch],str[len(str)-ch]=str[ch],str[len(str)-ch]

print(str)
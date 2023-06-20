def addSeries(n):
    bit = bin(n)
    bit = bit[2:]
    print(bit)
    temp_Bit = ''
    for i in bit:
        if i=='1':
            temp_Bit = temp_Bit+'0'
        else:
            temp_Bit = temp_Bit+'1'
    sum = 0
    for i in range(len(temp_Bit)):
        sum = sum + (int(temp_Bit[i])*(2**(len(temp_Bit)-(i+1))))
    return sum

nums = int(input("Nums:"))
print(addSeries(nums))
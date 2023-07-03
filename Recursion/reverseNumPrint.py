def reverseNumPrint(num,table_num):
    if num ==0:
        return 
    reverseNumPrint(num-1,table_num)
    print(num*table_num)

table=int(input("Table of: "))
reverseNumPrint(10,table)

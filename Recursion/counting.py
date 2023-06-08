num = int(input("Enter the Num: "))
def coun(num):
    if(num==0):
        return 1
    
    coun(num-1)
    print(num)

coun(num)
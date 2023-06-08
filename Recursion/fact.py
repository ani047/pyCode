num = int(input("Enter:"))

def fact(num):
    #base case
    if num==0:
        return 1
    

    #recursive relation 
    return num * fact(num-1)

n=fact(num)
print(n)

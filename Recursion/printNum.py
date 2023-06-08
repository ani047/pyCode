num = int(input("enters:"))

def display(num):
    if num == 0:
        return 1
    display(num-1)
   
    


display(num)
# create a function to implements the decorateters


def mainFunc(temp):
    print("Before code mass...")
    temp()
    print("After code mass...")
    
           
    
def dector():
    print("Hello")

mainFunc(dector)


def identifying(cubeAdd):
    a=int(input("a:"))
    b=int(input("b:"))
    c = int(input("c:"))
    def sum ():
        cubeAdd(a,b,c)
    
    sum()




def operationPerform(a,b,c):
    a=a**2
    b**=2
    c**=2
    add=a+b
    return add,c
identifying(operationPerform)

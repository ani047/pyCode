def table(n,number):
    if number==0:
        return 1
    table(n,number-1)
    print(n*number)

n = int(input("Enter the table:"))
number = 10
table(n,number)
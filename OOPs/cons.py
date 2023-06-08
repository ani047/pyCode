class Animal:
    

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __init__(self):
        print("This our Constructer")
    
    def show(self):
        print("Name is:",self.name)
        print("Age is :",self.age)

a2 = Animal()
a1=Animal("Cherry",8)

a1.show()

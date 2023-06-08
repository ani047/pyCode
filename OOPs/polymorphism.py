class Student:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city = city
    
    def disply(self):
        print("Name:",self.name)
        print("Age :",self.age)
        print("City:",self.city)


class College_Student(Student):
    def clg(self):
        print(self.name)
        print(self.age)
        print(self.city)

name = input("Enter the Name:")
age = int(input("Enter the Age :"))
city = input("Enter the City:")
s1 = College_Student(name,age,city)
s1.disply()
s1.clg()
class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def my_method(self,c=None):
        if c is None:
            return self.a+self.b
        return (self.a+self.b)/c
    
    def my_method(self):
        return self.a*self.b


obj = Parent(20,10)
print(obj.my_method()) #30
print(obj.my_method(30)) 
print(obj.my_method())

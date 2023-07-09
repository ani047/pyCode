class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def mymethod(self):
        return self.a+self.b
    

class child(parent):
    def __init__(self, a, b):
        super().__init__(a, b)

    def mymethod(self,c):
        if type(c)==str:
            return str(self.a)+str(self.b)+c
        else:
            return self.a+self.b+c


obj = child(25,10)
print(obj.mymethod(25))
print(obj.mymethod('23'))

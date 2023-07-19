class Implementations:
    def __init__(self,num) -> None:
        self.n = num
    

    def circleArea(self):
        return 3.14*self.n**2
    

    @staticmethod
    def add(a,b):
        return a+b
    
imp=Implementations(4)
print(imp.circleArea())
# print(Implementations.add(2,9))
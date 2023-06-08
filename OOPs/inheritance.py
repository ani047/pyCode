class Rectangle:
    def __init__(self,l,b):
        self.x=l
        self.b=b
    
    def areaRectangle(self):
        print("This is the Area of Rectangle",self.x*self.b)

class Triangle:
    def __init__(self,base,height):
        self.bs=base
        self.h=height

    def areaTriangle(self):
        print("This is the Area of Triangle",0.5*(self.bs*self.h))


class Area(Rectangle,Triangle):
    def show(self):
        super().areaRectangle()
        print("This is the Area Class")




A1=Area(2,8)
print(A1.areaRectangle())
A2=Area(4,6)
print(A2.areaTriangle())

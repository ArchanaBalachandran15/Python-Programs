
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass

class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name) 
        self.length=length
    def area(self):
        return self.length**2
    
class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

sq=Square("Square",6)
cir=Circle("Radius",3) 
print(sq.area())
print(cir.area())




    

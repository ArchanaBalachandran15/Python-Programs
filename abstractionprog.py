# Abstration Program

from abc import ABC, abstractmethod

# step 1: Abstraction

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# step 2 child class-Circle
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius * self.radius
    
# step 3 child class rectangle
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length= length
        self.width=width

    def area(self):
        return self.length* self.width
    
# step 4 use them
Cir= Circle(5)
print("area of circle:",Cir.area())

rectangle= Rectangle(6,4)
print("area of rectangle:",rectangle.area())
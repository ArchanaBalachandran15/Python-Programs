from abc import ABC,abstractmethod

class Polygon(ABC):

    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Rectangle(Polygon):
    def sides(self):
        print("Rectangle has 4 sides")

t=Triangle()
t=Rectangle()
t.sides()

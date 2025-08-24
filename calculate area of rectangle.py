#are of rectangle
class Rectangle:
    def __init__(self):
        self.length=0
        self.breath=0
    def area(self):
        self.length=int(input("enter the length: "))
        self.breath=int(input("enter the breath"))
        self.area=self.length*self.breath
    
    def print_data(self):
        print(self.area)
    
area1=Rectangle()
area1.area()
area1.print_data()


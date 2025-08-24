#oops program
class Bird:
    def __init__ (self):
        self.name=""
        self.color=""
    def eat(self):
        print("The bird eat ")
    def fly(self):
        print("The bird fly in high")

bird1=Bird()
bird1.eat()
bird1.fly()
    
class Car:
    def __init__(self):
        self.name=""
        self.color=""
        self.price=""
    def start(self):
        print("car is start")
    def stop(self):
        print("car is stop")
car1=Car()
car1.restart()
car1.returnstop()
# Inheritances Problem
# Fiveth Inheritances 
# Hybrid Inheritances  
# Hybrid Inheritanc: Combination of two or more types of inheritance.


# Example:1


print("......................")

# Example:2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.speak()
d.bark()

c = Cat()
c.speak()
c.meow()



#Using super() to Access Parent Class:

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls parent constructor
        print("Child Constructor")

obj = Child()
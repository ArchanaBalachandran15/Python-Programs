# Inheritances Problem
# First Inheritances 
# Single Inheritances  
# Single Inheritances: One child class inherits from One Parent Class.

# Example:1
class Person:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))

    def show(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.marks = int(input("Enter the marks: "))

    def show(self):
        super().show()  # Call the parent class show method
        print(self.marks)

# Create object of Student class
obj = Student()
obj.show()

print("......................")

# Example:1
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def display(self):
        print("This is the Child class.")

obj = Child()
obj.show()     # Inherited from Parent
obj.display()  # From Child

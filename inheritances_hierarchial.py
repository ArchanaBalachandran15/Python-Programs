# Inheritances Problem
# Fourth Inheritances 
# Hierarchial Inheritances  
# Hierarchical Inheritance:	Multiple child classes inherit from the Same Parent Class.

# Example:1

# Parent class
class Person:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))

    def show(self):
        print(self.name, self.age)

# Child class 1
class Student(Person):
    def __init__(self):
        super().__init__()
        self.marks = int(input("Enter the marks: "))

    def show(self):
        super().show()
        print(self.marks)

# Child class 2
class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.ph = input("Enter the phone number: ")

    def show(self):
        super().show()
        print(self.ph)

# Creating object of Student
obj1 = Student()
obj1.show()

# Creating object of Teacher
obj2 = Teacher()
obj2.show()


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

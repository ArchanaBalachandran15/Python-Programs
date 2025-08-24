# Inheritances Problem
# Third Inheritances 
# Multi_Level Inheritances  
# Multilevel Inheritance:	A class inherits from a class that itself inherited from another.

# Example:1

class Person:
    def __init__(self):
        self.fname = input("Enter the first name: ")
        self.lname = input("Enter the last name: ")

    def show(self):
        print("First name:", self.fname)
        print("Last name:", self.lname)

class Department:
    def __init__(self):
        self.did = input("Enter the department ID: ")
        self.dname = input("Enter department name: ")

    def show(self):
        print("Department ID:", self.did)
        print("Department Name:", self.dname)

class Student(Person, Department):  # Multiple Inheritance
    def __init__(self):
        Person.__init__(self)
        Department.__init__(self)
        self.id = input("Enter student ID: ")

    def show(self):
        Person.show(self)
        Department.show(self)
        print("Student ID:", self.id)

# Creating object of Student class
s1 = Student()
s1.show()


print("......................")

# Example:2

class Father:
    def skills(self):
        print("Father: Guitar and Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting and Dancing")

class Child(Father, Mother):
    def extra_skill(self):
        print("Child: Coding")

obj = Child()
obj.skills()       # From Father (method resolution order)
obj.extra_skill()

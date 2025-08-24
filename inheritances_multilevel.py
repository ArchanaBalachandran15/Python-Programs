# Inheritances Problem
# Second Inheritances 
# Multiple Inheritances  
# Multiple Inheritance:	One child class inherits from Multiple Parent Classes.

# Example:1
class Person:
    def __init__(self):
        self.fname = input("Enter the first name: ")
        self.lname = input("Enter the last name: ")

    def show(self):
        print("First name:", self.fname)
        print("Last name:", self.lname)


class Department(Person):
    def __init__(self):
        self.did = input("Enter the department id: ")
        self.dname = input("Enter department name: ")

    def show(self):
        print("Department ID:", self.did)
        print("Department Name:", self.dname)


class Student(Department):
    def __init__(self):
        Person.__init__(self)
        Department.__init__(self)
        self.id = input("Enter student id: ")

    def show(self):
        Person.show(self)
        Department.show(self)
        print("Student ID:", self.id)


# Creating object of Student class
s1 = Student()
s1.show()


print("......................")
# Example:2

class Grandparent:
    def heritage(self):
        print("Grandparent's heritage")

class Parent(Grandparent):
    def values(self):
        print("Parent's values")

class Child(Parent):
    def behavior(self):
        print("Child's behavior")

obj = Child()
obj.heritage()
obj.values()
obj.behavior()

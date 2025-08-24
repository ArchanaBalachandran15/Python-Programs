# Encapsulation Program

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__a = age       # private variable (data)

    def get_age(self):      # method to access data
        print(self.__a)

    def set_age(self, age): # method to modify data safely
        if age > 0:
            self.__a = age
            print("New age =", self.__a)
        else:
            print("Invalid age")

person = Person("Anil", 45)
person.get_age()       # Access through method
person.set_age(35)     # Modify through method


# # Encapsulation means binding data (variables) and methods (functions) that work on
# that data into a single unit (class), and
# restricting direct access to some of the object’s internal parts to protect it.

# a is private – can’t be accessed directly.
# We access it using methods: get_age()
# This protects the data

# #
# #

# Encapsulation means binding data (variables) and methods (functions) that work on that data into a single unit (class).
# It restricts direct access to some of the object’s internal parts to protect it.
# A variable with __ (double underscore), like __a, is private and cannot be accessed directly.
# You access or modify it using methods, like get_age() or set_age().
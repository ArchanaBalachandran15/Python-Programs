# Meethod OVER-Rindinng & Over Loading:
# # 1. Method Overriding (Run-time Polymorphism)
# Definition: A child class redefines a method of its parent class with the same name, number of arguments, and logic (can be different).
# When it happens: At runtime.
# Purpose: To change or extend the behavior of a parent class method.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overriding the parent method
        print("Dog barks")

# Test
obj = Dog()
obj.sound()  # Output: Dog barks


# # 2. Method Overloading (Compile-time Polymorphism)
# Definition: Having multiple methods with the same name but different number or type of parameters.
# Note: Python does not support true method overloading like Java or C++. Instead, you simulate it using default arguments or *args.
class Calculator:
    def add(self, a=0, b=0, c=0):
        print("Sum:", a + b + c)

# Test
obj = Calculator()
obj.add(10, 20)        # Output: Sum: 30
obj.add(1, 2, 3)       # Output: Sum: 6
obj.add()              # Output: Sum: 0


#Feature	                  Method Overriding	                                  Method Overloading
# Defined in	             Parent and Child class	                                     Same class
# Method name	             Same as parent method	                                     Same
# Arguments	                 Must be same	                                             Vary (number or type)
# Purpose	                 Modify behavior of inherited method                      	 Provide multiple ways to call a method
# Support                    in Python	✅ Yes	                                       Not directly (simulate using *args)
# Example Concept	         Inheritance	                                             Default parameters / *args
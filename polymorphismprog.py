# Polymorphism
# Built in Polumorphism
# Polymorphism = Same method or function name, different behavior

print(len("Hello"))      # Output: 5 (String)
print(len([1, 2, 3]))     # Output: 3 (List)
print(".........................................")

class Dog:
    def speak(self):
        return "Bark!"

class Cat:
    def speak(self):
        return "Meow!"
d = Dog()
c = Cat()

print(d.speak())   # Output: Bark!
print(c.speak())   # Output: Meow!

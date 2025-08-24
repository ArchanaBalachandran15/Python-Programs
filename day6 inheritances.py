# INHERITANCES
class Baseclass:
    def display(self):
        print("Hello")

class Subclass(Baseclass):  # Baseclass subclass silekku inheritances che u nnathu
    def Welcome(self):
        print("Welcome")

x=Baseclass()
x.display()
y=Subclass()
y.Welcome()
y.display()

print("..........")
print("..........")
print("SECOND PROBLEM Baseclass inhert the subclass")  

# Baseclass sill Variable varuna case
class Baseclass:
    def set_name(self,name):
        self.name=name

class Subclass(Baseclass):  # Baseclass subclass silekku inheritances che u nnathu
    def Welcome(self):
        print("Welcome")

    def display_name(self):
        print('Mariyum Bus Conductor Name is :',self.name)
        
y=Subclass()
y.Welcome()
y.set_name("Anil")
y.display_name()



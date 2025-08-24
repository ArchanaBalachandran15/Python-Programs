
# CONSTRUCTORS
# constructors used key word __int__

class Constructor1:
    def __init__(self):
        print("Good Morning")
x=Constructor1()
y=Constructor1()
print(".............")
print(".............")


# Arugument passing inside the constructor
class Constructor2:
    def __init__(self,name,age,place):
          self.uniquename=name
          self.era=age
          self.location=place
    
    def display(self):
        print("Name  :"  , self.uniquename)
        print("Age   :"   , self.era)
        print("Place :" , self.location)

a=Constructor2("Robin",45,"Petta")
b=Constructor2("Ani",40,"Pala")
a.display()
print(".............")
print(".............")
b.display()

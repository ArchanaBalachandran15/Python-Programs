#multi level inheritances

class Animal:
    def speaking(self):
        print("Animals are speak")
    
class Dog(Animal):
    def watchman(self):
        print("Doges are the watch man of every houses")

class Child_Dog(Dog):
    def pet(self):
        print("Dog child are the pet of humans")
d=Child_Dog()
d.watchman()
d.pet()
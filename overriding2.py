class Animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        pass

class Dog(Animal):
    def __init__(self, name,sound):
        super().__init__(name)
        self.sound=sound
    def info(self):
        pass

class Cat(Animal):
    def __init__(self, name,hair):
        super().__init__(name)
        self.hair=hair
    def info(self):
        pass

dg=Dog("sd,bow")
ct=Cat("edc,white ")
print(dg.sound(" "))
print(dg.info())

print(ct.hair(" "))
print(ct.info())
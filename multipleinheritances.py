#multiple level inheritances

class Parent_class1:
    def __init__(self,name):
        self.name=name
    def addition(self,a,b):
        return a+b
    def info(self):
        print('Parent_class1')

class Parent_class2:
    def __init__(self,type):
        self.type=type
    def multiplication(self,a,b):
        return a*b
    def info(self):
        print('Parent_class2')
    def division(self,a,b):
        return a/b

class Derived(Parent_class1,Parent_class2):
    pass


d=Derived("")
d.info()
print(d.addition(20,30))
print(d.multiplication(10,20))

    
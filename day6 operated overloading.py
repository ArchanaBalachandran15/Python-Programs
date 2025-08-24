# Operatind Overloading

class Operatedoverloading:
    def set_name(self,name):
        self.name=name

    def __add__(self,other):             # operater overloading method ket word is __add__
        name=self.name+" "+other.name
        return name

first_name=Operatedoverloading()
second_name=Operatedoverloading()

first_name.set_name("Anil")
second_name.set_name("Chandran")

full_name=first_name+second_name         # purposes
print(full_name)





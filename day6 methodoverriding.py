# METHOD OVERRIDING
class Baseclass:
    def __init__(self):      #constructor
        print("Base Init")

    def set_name(self,name):
        self.name=name
        print("Baseclass set name")

class Subclass(Baseclass):          # Baseclass subclass silekku inheritances che u nnathu
    
    def __int__(self):             # method 1
        Baseclass.__int__(self)    # base class sienthe int tinne call che u nnathu
    
    def __int__(self):              # METHOD 2
        super().__int__()
        print("BASE CLASS INIT")

    def __init__(self):             #constructor Evide Subclass sienthe init mathram me work che u nnullu That process is called OVERRIDING
        print("Subclass Init")
    
    def Welcome(self):
        print("Welcome")

    def set_name(self,name):
        self.name=name
        print("Subclass set name")

    def display_name(self):
        print('Mariyum Bus Conductor Name is:',self.name)
        
y=Subclass()
y.Welcome()
y.set_name("Anil Chandran")
y.display_name()




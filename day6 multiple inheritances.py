# MULTIPLE INHERITANCES

class First:
    def display_first(self):
        print("Good Evening")

class Second:
    def display_second(self):
        print("Lunchy Time")

class Third(First,Second):     # First & Second class inherited in third class
    def dispaly_third(self):
        print("Third")

z=Third()
z.display_first()
z.display_second()
z.dispaly_third()
print("..................")
print("..................")
print("..................")

#Another Way Above pro =g was some problem that was solved in this prog

class First:
    def display(self):
        print("Good Evening")

class Second:
    def display(self):
        print("Lunchy Time")

class Third(Second,First):     
    def dispaly_third(self):
        print("Third")

class Third(First,Second):     
    def dispaly_third(self):
        print("Third")

z=Third()
z.display()
z.dispaly_third()
print(Third.mro())   # yethiu class sienthe order annu ariyedathu ennu nokkan class name.mro ennuu koduthal mathi

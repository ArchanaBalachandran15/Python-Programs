# MULTILEVEL INHERITANCES

class First:
    def display_first(self):
        print("Good Evening")

class Second(First):
    def display_second(self):
        print("Lunchy Time")

class Third(Second):     
    def dispaly_third(self):
        print("Third")

z=Third()
z.dispaly_third()
z.display_first()
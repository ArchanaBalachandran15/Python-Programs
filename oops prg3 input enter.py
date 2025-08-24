#input enter 
class Bird:
    def __init__ (self):
        self.name=""
        self.color=""
        self.beak_color=""

    def bird_data(self):
        self.name=input("Enter the Name of the bird: ")
        self.color=input("Enter the color of the bird: ")
        self.beak_color=input("Enter the beak colour of the bird: ")

    def print_data(self):
        print(self.name,self.color,self.beak_color)

bird1=Bird()
bird1.bird_data()
bird1.print_data()


bird2=Bird()
bird2.bird_data()
bird2.print_data()


bird3=Bird()
bird3.bird_data()
bird3.print_data()




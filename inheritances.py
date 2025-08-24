#single inheritances
class Animal:
    def __init__(self,Name,color):
        self.name=Name
        self.colour=color
    def info (self):
            print(self.name+"s",+"color is ", self.colour)

class Bird(Animal):
#To add one more attribute
    def __init__(self, Name, color, Bkcolor):
        super().__init__(Name,color)
        self.bkcolor=Bkcolor
    def fly(self):
        print("Bird can fly")
 


    




        

        
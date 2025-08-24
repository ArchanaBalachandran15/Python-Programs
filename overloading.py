class Car:
    def move(self):
        print("Drive")

class Ship:
    def move(self):
        print("Sail")

class Plane:
    def move(self):
        print("Fly")

class Train:
    def move(self):
        print("Magnet")

c=Car()
s=Ship()
p=Plane()
t=Train()
for i in(c,s,p,t):
    i.move()

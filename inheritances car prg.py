#single inheritances

class Vehicle:
    def __init__(self,brd,num):
        self.brand=brd
        self.number=num
    def data(self):
        print(self.brand,self.number)

class Car(Vehicle):
    def __init__(self, brd,num,nme):
        super().__init__(brd, num)
        self.name=nme

    def print_data(self):
        print("Brand name of the vehicle: ",self.name)

    def start(self):
        print("Car is starting")
car=Car("India","230597","BMW")
car.data()
car.print_data()
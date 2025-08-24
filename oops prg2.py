#creating class with arguments
class Bird:
   def __init__ (self,nme,clr,bkclr):
        self.name=nme
        self.color=clr
        self.beak_color=bkclr


bird1=Bird("crow","black","grey")
print(bird1.name)
print(bird1.color)
print(bird1.beak_color)


bird2=Bird("parrot","green","red")
print(bird2.name)
print(bird2.color)
print(bird2.beak_color)


bird2=Bird("pigeon","green","grey")
print(bird2.name)
print(bird2.color)
print(bird2.beak_color)

#multiple object creation
birds=[]
for i in range(5):
    obj=birds()
    birds.append(obj)
for i in birds:
    i.birds_data()
    i.print_data()
    
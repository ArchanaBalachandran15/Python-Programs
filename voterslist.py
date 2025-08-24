# create the voters list
class Person:
    def __init__(self):
        self.name=""
        self.age=0

    def voters_list(self):
        self.name=input("Enter the name of the person: ")
        self.age=int(input("Enter the age of the person: "))
    
    def check_eligible(self):
        if self.age>=18:
            self.res="eligible"
        else:
            self.res="not eligible"
    
    def display_details(self):
        print(self.name,"\t",self.age,"\t",self.res)

vote=[]
for i in range(3):
    obj=Person()
    vote.append(obj)
    obj.voters_list()
    obj.check_eligible()
for i in vote:
    i.display_details()

        
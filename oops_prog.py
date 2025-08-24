# Object oriented programm

# class Student:
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#     def study(self):
#         print(self.n,self.r)

# s1=Student("Amal",1011)
# s2=Student("Libin",1012)
# s1.study()
# s2.study()

# User udde aduthu ninum input vanjikkunnathu
class Myclass:
    def __init__(self):
        self.n=input("Enter the Name: ")
        self.reg=int(input("Enter the Rollno: "))
        self.ag=int(input("Enter the Age: "))
    def display(self):
        print(self.n,self.reg,self.ag)
obj=Myclass()
obj.display()


# another example
class Employee:
    def __init__(self):
        self.empname=input("Enter the Employee Name: ")
        self.empcode=int(input("Enter the Employee Code: "))
        self.empdep=(input("Enter the department of the Employee: "))
        self.empage=int(input("Enter the Age of the Employee: "))
    def Present(self):
        print(self.empname,self.empcode,self.empdep,self.empage)
obj1=Employee()
obj1.Present()
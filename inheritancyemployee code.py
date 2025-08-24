#single inheritances

class Company:
    def __init__(self,nme,id_number):
        self.name=nme
        self.number=id_number
    
    def details(self):
        print(self.name,self.number)

class Employee(Company):
    def __init__(self,nme,id_number,position,salary): 
        super().__init__(nme,id_number)
        self.post=position
        self.wage=salary
    
    def print_data(self):
        print("Position of the Employee:",self.post)
        print("Salary of the Employee:",self.wage)
    
emp=Employee("John","id_no:1508","Manager","20000")
emp.details()
emp.print_data()
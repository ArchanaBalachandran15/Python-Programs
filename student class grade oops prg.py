# create the student class
class Student:
    def __init__(self):
        self.name=""
        self.roll_number=0
        self.mark1=0
        self.mark2=0
        self.mark3=0
        self.total=0
        self.ave=0
        self.grade=''
        

    def student_data(self):
        self.name=input("Enter the name of the student")
        self.roll_number=int(input("Enter the roll number of the student"))
        self.mark1=int(input("Enter the mark1 of the student"))
        self.mark2=int(input("Enter the mark2 of the student"))
        self.mark3=int(input("Enter the mark2 of the student"))
        self.total=(self.mark1+self.mark2+self.mark3)
        self.ave=self.total/3

    def cal_grade(self):
        if self.ave>=90 and self.ave<=100:
            self.grade="Grade A"
        elif self.ave>=80 and self.ave<=89:
            self.grade="Grade B"
        elif self.ave>=70 and self.ave<=79:
            self.grade="Grade C"
        elif self.ave>=60 and self.ave<=69:
            self.grade="Grade D"
        else:
            self.grade=" Fail"

    def display_details(self):
        print(self.name,"\t",self.roll_number,"\t",self.total,"\t",self.ave,"\t",self.grade)

student=[]
for i in range(3):
    obj=Student()
    student.append(obj)
    obj.student_data()
    obj.cal_grade()

for i in student:
    i.display_details()

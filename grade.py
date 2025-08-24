#Task Day-11
#Question number 1

mark1=int(input("enter the mark1"))
mark2=int(input("enter the mark2"))
mark3=int(input(" enter the mark3"))
ave=(mark1+mark2+mark3)/3
print(ave)
if ave>=90 and ave<=100:
    print("Grade A")
elif ave>=80 and ave<=89:
    print("Grade B")
elif ave>=70 and ave<=79:
    print("Grade C")
elif ave>=60 and ave<=69:
    print("Grade D")
else:
    print(" Fail")
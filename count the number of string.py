list1=["hello","good","morning","how","are","you",'nnn']
for i in list1:
    if len(i)>=2 and i[0]==i[-1]:
        print(i)
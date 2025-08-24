from phonebook import*
while(True):
    print("menu")
    print("1.Add\n" "2.update\n" "3.delete\n" "4.display\n")
    option=int(input("enter the option"))
    if option==1:
        cont_add()
    elif option==2:
        cont_update()
    elif option==3:
        cont_display()
    elif option==4:
        cont_delete()
    else:
        f=open("cont.txt","a")
        for i,j in cont.items():
            f.write(i+":"+str(j)+"\n")
        exit()


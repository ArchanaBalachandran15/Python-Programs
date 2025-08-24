cont={}
def cont_add():
        name=(input("enter the name"))
        number=int(input("enter the number"))
        if name in cont:
            print("this name already existed")
        else:
            cont[name]=number
            print(cont)

def cont_update():
    newoption=int(input("enter the input"))
    if newoption==1:
            oldname=input("enter old name")
            newname=input("change the key")
            cont[newname]=cont.pop(oldname)
            print(cont)

    elif newoption==2:
            number=input("enter the number")
            name=input("enter the name")
            cont[name]=number
def cont_display():
    print(cont)


def cont_delete():
    name1=int(input("enter the name"))
    cont.pop(name1)
    print(cont)


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
         exit()


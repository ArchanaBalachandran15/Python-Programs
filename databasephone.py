import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db200"
    )

    mycursor=con.cursor()
    name=input(" ")
    number=int(input(" "))
    #mycursor.execute("create table phone_book (id int auto_increment primary key,name varchar(10),phone_number bigint)")
    print("Menu \n 1.Add \n 2.Update \n 3.Delete \n 4.Display \n 5.Start")
while (True):
    opt=int(input("choose option: "))
    if opt==1:
        name=input("enter name: ")
        pho=int(input("enter phone number: "))
        mycursor.execute("insert into phone_book (name,pho)(%s,%s)",(name,pho))
        print("Inserted")
            # to check existing name 
        mycursor.execute("select name from phone_book: ")
        name=mycursor.fetchall()
        f=0
        for i in name:
            if name==i[0]:
                f=1
            if f==0:
                mycursor.execute("insert into phone_book(name,pho)values%s",(name,pho))
                con.commit()
            else:
                print("name already existing")

    if opt==2:
        print("1.name,2.phone_number")
        cha=int(input("enter option: "))
        if cha==1:
            old=input("enter old name: ")
            new=input("enter new name: ")
            mycursor.execute("update phone_book set name=%s where name%s",(new,old))
            con.commit()
            print("updated")
        if cha==2:
            old_ph=input("enter old_ph: ")
            new_ph=input("enter new_ph: ")
            mycursor.execute("update phone_book set pho=%s where pho%s",(new_ph,old_ph))
            con.commit()
            print("updated")
    if opt==3:
        id=int(input("enter the id to be deleted: "))
        mycursor.execute("delete from phone_book where id=%s",(id,))
        con.commit()
        print("deleted")
    if opt==4:
        mycursor.execute("select * from phone_book")
        res=mycursor.fetchall()
        print(res)
    if opt==5:
        (exit)




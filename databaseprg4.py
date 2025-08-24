import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db70000"
    )

    mycursor=con.cursor()
    mycursor.execute("select * from employee where id=3")
    result_list=mycursor.fetchall()
    result_list2=mycursor.fetchone() # only single value print function
    print(result_list2)
    print(result_list)

    #delete operation
    name=input("Enter the input: ")
    mycursor.execute("delete from employee where name=%s",(name,))
    print("record delete")
    con.commit()

    # update
    name=input("Enter the name: ")
    mycursor.execute("update yee set name=%s,name=achee where name")

    for i in result_list2:
        print(i)
except Exception as e:
    print(e)


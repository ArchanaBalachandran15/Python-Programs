import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db100"
    )

    mycursor=con.cursor()
    name=input(" ")
    address=input(" ")
    mycursor.execute("insert into employee (name,address)values(%s,%s)",(name,address))
    con.commit()
    print("created")
except Exception as e:
    print(e)
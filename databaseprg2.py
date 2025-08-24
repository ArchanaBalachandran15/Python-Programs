import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db100"
    )


    mycursor=con.cursor()
    mycursor.execute('create table employee(id int auto_increment primary key,name varchar(10),address varchar(10))')
    print('db created')

except Exception as e:
    print(e)


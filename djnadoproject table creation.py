import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db800"
    )


    mycursor=con.cursor()
    mycursor.execute('create table collection of data(id int auto_increment primary key,name varchar(255),price(double),description varchar(150))')
    print('db created')

except Exception as e:
    print(e)
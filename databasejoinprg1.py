#mysql join problem

import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db300"
    )
    mycursor=con.cursor()

    sql="Select users.name as user, products.name as fov from users inner join products on users.fav=products.id"
    mycursor.execute(sql)
    my_result=mycursor.fetchall()
    for x in my_result:
        print(x)
except Exception as e:
    print(e)




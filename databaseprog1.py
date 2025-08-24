# data base prog

import pymysql
try:
    con=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
    )


    mycursor=con.cursor()
    mycursor.execute('create database db2100')
    print('db created')

except Exception as e:
    print(e)






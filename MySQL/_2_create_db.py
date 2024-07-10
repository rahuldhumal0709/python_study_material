import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="Rahul",password="Rahul@0709")
my_cursur=mydb.cursor()
my_cursur.execute("CREATE DATABASE db1")
# mydb.commit()
# mydb.close()
# print("MySQL connectivity succesfull")
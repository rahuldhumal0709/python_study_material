import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="Rahul",password="Rahul@0709")
print(mydb.connection_id)
my_cursur=mydb.cursor()
mydb.commit()
mydb.close()
print("MySQL connectivity succesfull")
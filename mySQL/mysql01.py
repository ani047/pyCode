import mysql.connector
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "H4CK9847"
)


myCursor = mydb.cursor()

#myCursor.execute(" CREATE DATABASE eCommerce")

myCursor.execute("show databases")

for x in myCursor:
    print(x)

import mysql.connector
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "H4CK9847",
    database="ecommerce"
)

myCursor = mydb.cursor()

#myCursor.execute(" CREATE DATABASE eCommerce")
def is_create_db():
    myCursor.execute("create table ")
myCursor.execute("show databases")
for x in myCursor:
    print(x)



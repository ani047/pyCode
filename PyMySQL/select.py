import mysql.connector
import mysql

cnx = mysql.connector.connect(
    localhost = "localhost",
    user = "root",
    password = "H4CK9847",
    database = "employee_management"
)

cursor = cnx.corsor()

query = "select * from employee"

cursor.execute(query)


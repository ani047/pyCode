import mysql.connector
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "H4CK9847",
    database="ecommerce"
)
myCursor = mydb.cursor()
def createTable():
    myCursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255),address VARCHAR(255))")
i=0
if i<1:
    createTable()

def insertData():

    sql = "INSERT INTO customers (first_name, last_name address) VALUES (%s, %s)"
    val = ("ram","Kumar" "Highway 21")

    myCursor.execute(sql, val)

    mydb.commit()

    print(myCursor.rowcount, "record inserted.")
# createTable()
# insertData()
print(myCursor.rowcount, "record inserted.")
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="53idisan",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

mycursor.close()
mydb.close()
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="53idisan",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

mycursor.close()
mydb.close()
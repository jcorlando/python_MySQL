import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "mydatabase"
	)

mycursor = mydb.cursor()

# Use ALTER when the table already exists
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



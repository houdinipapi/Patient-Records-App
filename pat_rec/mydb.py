import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234@adMIN"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS patientrecords")

# cursorObject.execute("USE patientrecords")

print("Database created successfully!")
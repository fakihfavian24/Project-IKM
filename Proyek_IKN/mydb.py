import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE proyek_ikn")

# print jika database berhasil dibuat
print("Database created successfully")
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'miki',
    password = '67716914',
)


conn = dataBase.cursor()

conn.execute("CREATE DATABASE users")

print("DONE!")

# Close the connection

conn.close()

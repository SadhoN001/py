## pip install mysql-connector-python
import mysql.connector #Imports the module needed to interact with a MySQL database from Python.

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password='Sadhon123#',
    # database='sadhondb'
)

mycursor= mydb.cursor() # A cursor allows you to execute SQL commands on the database connection.
# mycursor.execute("CREATE DATABASE sadhondb")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

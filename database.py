## pip install mysql-connector-python
import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user=" root",
    password='Sadhon123#',
    # database='sadhondb'
)

mycursor= mydb.cursor()
# mycursor.execute("CREATE DATABASE sadhondb")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

print("dog")

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="sql1",
    passwd="Cirica01@@Parolafmm123@@",
    port="1433"
)

print(db)
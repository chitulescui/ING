import os

# my_var = os.environ["MY_VAR"]

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd=os.environ.get('MYSQL_ROOT_PASSWORD'),
    port="3306",
    auth_plugin='mysql_native_password'
)

print(db)
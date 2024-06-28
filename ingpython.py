import os

# my_var = os.environ["MY_VAR"]

import mysql.connector

db = mysql.connector.connect(
    host=os.environ.get("HOST"),
    user=os.environ.get("USER"),
    passwd=os.environ.get('MYSQL_ROOT_PASSWORD'),
    port=int(os.environ.get("PORT")),
    auth_plugin=os.environ.get("AUTH_PLUGIN")
)

print(db)
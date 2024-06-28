import os

# my_var = os.environ["MY_VAR"]

import mysql.connector

host=os.environ.get("HOST"),
user=os.environ.get("USER"),
passwd=os.environ.get('MYSQL_ROOT_PASSWORD'),
port=int(os.environ.get("PORT")),
auth_plugin=os.environ.get("AUTH_PLUGIN")

def connect_to_database(host, user, password, port, auth_plugin):
    db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=port,
        auth_plugin=auth_plugin
    )
    return db
connect_to_database(host, user, passwd, port, auth_plugin)


print(db)


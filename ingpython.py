import os

# my_var = os.environ["MY_VAR"]

import mysql.connector

host=os.environ.get("HOST"),
user=os.environ.get("USER"),
password=os.environ.get('MYSQL_ROOT_PASSWORD'),
port=int(os.environ.get("PORT")),
auth_plugin=os.environ.get("AUTH_PLUGIN")
database=os.environ.get("DATABASE")

def connect_to_mysql(host, user, password, port, auth_plugin):
    db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=port,
        auth_plugin=auth_plugin
    )
    return db

def connect_to_database(host, user, password, port, auth_plugin,database):
    db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=port,
        auth_plugin=auth_plugin,
        database=database
    )
    return db

def create_a_database():
    mycursor= db.cursor()
    mycursor.execute("CREATE DATABASE testdatabase")

connect_to_mysql(host, user, password, port, auth_plugin)
create_a_database()
connect_to_database(host, user, password, port, auth_plugin,database)


print(db)


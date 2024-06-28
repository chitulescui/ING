from credentials import host, user, password, sqlport, auth_plugin
# my_var = os.environ["MY_VAR"]
import mysql.connector
import os
from mysql.connector import Error, connect


# host = os.environ.get("HOST")
# user = os.environ.get("USER")
# password = os.environ.get('MYSQL_ROOT_PASSWORD')
# port = int(os.environ.get("PORT"))
# auth_plugin = os.environ.get("AUTH_PLUGIN")
# database = os.environ.get("DATABASE")

def printfunc():
    for x in cursor:
        print(x)

def connect_to_mysql(host, user, password, sqlport, auth_plugin):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=sqlport,
        auth_plugin=auth_plugin
    )
    return connection



def create_database():
    database_name = input("Choose a name for your database")
    if type(database_name) is not str:
        print("Your Database name is not valid, string needed")
        create_database()
    elif len(database_name) < 8 or len(database_name) > 20:
        print("Your Database name should contain a maximum of 20 characters and a minimum of 8 characters")
        create_database()
    elif database_name:
        print("Invalid input, please repeat the process")
        create_database()
    else:
        with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE " +database_name)

try:
    connect_to_mysql(host, user, password, sqlport, auth_plugin)
    create_database()


except Error as e:
    print(e)

# create_db_query = "CREATE DATABASE online_movie_rating"
        # create_table ="CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"
        # # create_db_queryy="DROP DATABASE online_movie_rating"
        # with connection.cursor() as cursor:
        #     # cursor.execute(create_db_query)
        #     # cursor.execute(create_db_query)
        #     cursor.execute("USE online_movie_rating")
        #     cursor.execute(create_table)
        #     cursor.execute("DESCRIBE Person")
        #     printfunc()
        #     print("a ajuns pana aici")





# def create_a_database():
#     mycursor = db.cursor()
#     mycursor.execute("CREATE DATABASE testdatabase")


# connect_to_mysql(host, user, password, port, auth_plugin)
# create_a_database()
# connect_to_database(host, user, password, port, auth_plugin, database)



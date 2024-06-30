import mysql.connector
import os
from mysql.connector import Error, connect
host = "127.0.0.1"
user = "root"
password = "Cirica01@@"
sqlport = "3306"
auth_plugin = "mysql_native_password"

# def connect_to_mysql(host, user, password, sqlport, auth_plugin):
#     global connection
#     connection = mysql.connector.connect(
#     host=host,
#     user=user,
#     passwd=password,
#     port=sqlport,
#     auth_plugin=auth_plugin
#     )


def connect_to_database(host, user, password, sqlport, auth_plugin):
    global connection
    global mycursor

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            port=sqlport,
            auth_plugin=auth_plugin
        )
        if connection.is_connected():
            mycursor = connection.cursor()
            print("Connected to MySQL database")
    except Error as err:
        print(f"Error: '{err}'")
        connection = None
    return connection

def create_database(connection):
    global database_name
    while True:
        try:
            database_name = input("Choose a name for your database: ")
            if len(database_name) == 0:
                raise ValueError("Your database name cannot be empty")
            elif not database_name.isalpha():
                raise ValueError("Your database name cannot contain numbers or special characters")
            elif len(database_name) < 8 or len(database_name) > 20:
                raise ValueError(
                    "Your database name should contain a maximum of 20 characters and a minimum of 8 characters")

            mycursor = connection.cursor()
            mycursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Your database {database_name} was created successfully")
            mycursor.execute(f"USE {database_name}")
            print(f"Your are using the new database {database_name}")
            return database_name
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def table_structure():
    mycursor.execute(f"USE {database_name}")
    table_list=["Chitulescu","Victorian","Cocochanela"]
    for tabel in table_list:
       mycursor.execute(f"CREATE TABLE {tabel} (name VARCHAR(50), age smallint UNSIGNED, city VARCHAR(50))")



def insert_info():
    mycursor.execute("USE cacatdebazadedate")
    mycursor.execute(f"INSERT INTO chitulescu (name, age, city) VALUES ('guta', 31, 'Bucuresti');")

    mycursor.execute("SELECT * FROM chitulescu")
def tojson():
    mycursor.execute("SELECT name AS 'name',age AS 'age', city AS 'city' FROM chitulescu FOR JSON PATH;")

tojson()

cocds= mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE'")

    connection.commit()
    
try:
    connect_to_database(host, user, password, sqlport, auth_plugin)
    create_database(connection)
    table_structure()


except Error as e:
    print(e)









# def create_database():
#     database_name = input("Choose a name for your database")
#         if len(database_name)==0 :
#             print("Your database name cannot be empty")
#             create_database()
#         elif database_name.isalpha():
#             if len(database_name) < 8 or len(database_name) > 20:
#                 print("Your Database name should contain  a maximum of 20 characters and a minimum of 8 characters")
#                 create_database()
#             elif not database_name:
#                 print("Invalid input, please repeat the process")
#                 create_database()
#             else:
#                 mycursor = connection.cursor()
#                 mycursor.execute(f"CREATE DATABASE {database_name}")
#                 print(f"Your Database {database_name} was created successfully")
#                 return database_name
#         else:
#             print("your database name cannot contain numbers")
#             create_database()


import pyodbc
from credentials import SERVER, PASSWORD, USERNAME
import os

def create_connection(server, username, password):
    connection_str = (
        f'DRIVER={{ODBC Driver 18 for SQL Server}};'
        f'SERVER={server};'
        f'UID={username};'
        f'PWD={password};'
        f'TrustServerCertificate=yes;'
    )
    try:
        connection = pyodbc.connect(connection_str)
        print("Connection successful!")
        return connection
    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        return None


# def create_database():
#     database_name = input("Choose a name for your database")
#     if type(database_name) is not str:
#         print("Your Database name is not valid, string needed")
#         create_database()
#     elif len(database_name) < 8 or len(database_name) > 20:
#         print("Your Database name should contain a maximum of 20 characters and a minimum of 8 characters")
#         create_database()
#     elif database_name:
#         print("Invalid input, please repeat the process")
#         create_database()
#     else:
#         with connection.cursor() as cursor:
#             cursor.execute(f"CREATE DATABASE {database_name} ")
#             return database_name

# try:
    create_connection(SERVER, USERNAME, PASSWORD)
    # create_database()

#
# except Error as e:
#     print(e)
#
# create_db_query = "CREATE DATABASE online_movie_rating"
#         create_table ="CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"
#         # create_db_queryy="DROP DATABASE online_movie_rating"
#         with connection.cursor() as cursor:
#             # cursor.execute(create_db_query)
#             # cursor.execute(create_db_query)
#             cursor.execute("USE online_movie_rating")
#             cursor.execute(create_table)
#             cursor.execute("DESCRIBE Person")
#             printfunc()
#             print("a ajuns pana aici")





# def create_a_database():
#     mycursor = db.cursor()
#     mycursor.execute("CREATE DATABASE testdatabase")


# connect_to_mysql(host, user, password, port, auth_plugin)
# create_a_database()
# connect_to_database(host, user, password, port, auth_plugin, database)



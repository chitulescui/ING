import pyodbc
import json
import os
from credentials import SERVER, PASSWORD, USERNAME, DATABASE, TABLE


# SERVER=".,1433"
# PASSWORD="Cirica01@@"
# USERNAME="sa"
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 22]
cities = ['New York', 'Los Angeles', 'Chicago']

def create_connection(server, username, password):
    global connection, cursor
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
        connection.autocommit = True
        cursor=connection.cursor()
        return connection, cursor
    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        return None



# Create the database
def create_database(DATABASE,TABLE):
    try:
        cursor.execute(f"CREATE DATABASE {DATABASE}")
        print("Database created or already exists.")
        cursor.execute(f"USE {DATABASE}")
        print("Using the database.")
    except pyodbc.Error as e:
        return None
        
    try:
        cursor.execute(f"CREATE {TABLE}  (name VARCHAR(50), age smallint, city VARCHAR(50) )")
        print("Table created ")
    except pyodbc.Error as e:
        print("Error creating the database:", e)
        return None



def populate_table(names, ages, cities):
    # Ensure the lists have the same length
    if not (len(names) == len(ages) == len(cities)):
        raise ValueError("All input lists must have the same length")
    for name, age, city in zip(names, ages, cities):
        cursor
        cursor.execute(f"INSERT INTO {TABLE} (name, age, city) VALUES (?, ?, ?)", (name, age, city))

create_connection(SERVER, USERNAME, PASSWORD)
create_database(DATABASE,TABLE)
populate_table(names,ages,cities)



cursor.execute("SELECT name AS 'name', age AS 'age', city AS 'city' FROM Person1 FOR JSON PATH;")
json_result = cursor.fetchone()[0]
json.loads(json_result)
with open('ingdatabase.json', 'w') as f:
    json.dump(json.loads(json_result), f, indent=4)

print("haidaviatamea")


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



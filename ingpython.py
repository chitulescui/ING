import pyodbc, json, os
from credentials import SERVER, PASSWORD, USERNAME, DATABASE, JSON_NAME
from variables import names, ages, cities, tables

#Create the connection to SQL Server
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



# Create the and select the Database.
def create_database(DATABASE):
    try:
        cursor.execute(f"CREATE DATABASE {DATABASE}")
        print("Database created or already exists.")
        cursor.execute(f"USE {DATABASE}")
        print(f"Using the {DATABASE} database.")
    except pyodbc.Error as e:
        print("Database cannot be created:", e)
        return None

#Create the tables.
def create_table(tables):
    try:
        for table in tables:
             cursor.execute(f"""CREATE TABLE {table} 
                            (name VARCHAR(50), 
                            age smallint, 
                            city VARCHAR(50))""")
             print(f"Table {table} created ")
    except pyodbc.Error as e:
        print("Table cannot be created:", e)
        return None


#Populate the tables.
def populate_tables(names, ages, cities):
    try:
        for table in tables:
            # Ensure the lists have the same length
            if not (len(names) == len(ages) == len(cities)):
                raise ValueError("All input lists must have the same length")
            for name, age, city in zip(names, ages, cities):
                cursor.execute(f"""INSERT INTO {table} (name, age, city) 
                               VALUES (?, ?, ?)""", (name, age, city))
            print("Table populated successfully!")
    finally: 
        print("Tables have been populated")

#Export the table.
def export_table():
    cursor.execute(f"""SELECT name AS 'name', age AS 'age', city AS 'city' 
                   FROM {tables[0]} FOR JSON PATH;""")
    json_result = cursor.fetchone()[0]
    with open(f'{JSON_NAME}.json', 'w') as f:
        json.dump(json.loads(json_result), f, indent=4)
        print(f"{JSON_NAME} file created successfully!")

#Close the connection with the Database.
def close_connection():
    cursor.close()
    connection.close()


#Function Calls 
try:
    create_connection(SERVER, USERNAME, PASSWORD)
    create_database(DATABASE)
    create_table(tables)
    populate_tables(names,ages,cities)
    export_table()
except pyodbc.Error as e:
    print("You have an error:", e)
finally: 
    close_connection()
    print("Connection closed")








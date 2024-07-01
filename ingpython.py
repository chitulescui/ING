#Import Libraries 
import pyodbc, json, os, random
from os.path import exists
from credentials import SERVER, PASSWORD, USERNAME, DATABASE, JSON_NAME
from variables import names, ages, cities, tables

#Create the connection to SQL Server

def create_connection(server, username, password):
    global connection, cursor                       #Globally declared variables in order to use them in the next functions.
    connection_str = (
        f'DRIVER={{ODBC Driver 18 for SQL Server}};'
        f'SERVER={server};'
        f'UID={username};'
        f'PWD={password};'
        f'TrustServerCertificate=yes;'
    )
    try:
        connection = pyodbc.connect(connection_str)  #Establish the connection with the Database.
        print("Connection successful!")
        connection.autocommit = True
        cursor=connection.cursor()                   #Creating the cursor in order to execute next SQL queries 
        return connection, cursor
    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        return None


# Create and select the Database.

def create_database(database=DATABASE):                     
    try:                                              #Creating the database and checks if the database already exists or not. 
        cursor.execute(f"""
                        BEGIN CREATE DATABASE {database}
                        END""")
        connection.commit()
        print("Database created.")
        cursor.execute(f"USE {database}")
        print(f"Using the {database} database.")
    except pyodbc.Error as e:
        if "42000" in str(e):
            print(f"Error '42000': Database '{database}' already exists")
            return None

#Create the tables.

def create_table(tables):                              
    try:                                               #Creating the table and checks if the table already exists or not in the database.
        for table in tables:
             cursor.execute(f"""CREATE TABLE {table} 
                            (name VARCHAR(50), 
                            age smallint, 
                            city VARCHAR(50))""")
             print(f"Table {table} created ")
    except pyodbc.Error as e:
        if "42S01" in str(e):
            print(f"Error '42S01':There is already an object named {table} in the database. ")
            return None


#Populate the tables.

def populate_tables(names, ages, cities):               
    try:                                               #Populate the table with values from 3 lists(names, ages, cities).
        for table in tables:
            # Ensure the lists have the same length
            if not (len(names) == len(ages) == len(cities)):
                raise ValueError("All input lists must have the same length")
            for name, age, city in zip(names, ages, cities):
                cursor.execute(f"""                                
                                   INSERT INTO {table} (name, age, city) 
                                   VALUES (?, ?, ?)
                                   """, (name, age, city))
        print("Table populated successfully!")
    except pyodbc.Error as e:
            print("Error '42S01':Invalid object name",str(e))
            return None
    # finally:
    #     print("Tables have been populated")


#Export table in JSON format.

def export_table():
    try:
        file_exists = os.path.exists(f'{JSON_NAME}') #Check if the file with the same name exists or not.
        if file_exists == True:
            print(f"{JSON_NAME} already exists!")
        else:
            table_number = random.choice(range(len(tables)))  # Create a random number within the range of the tables list.
            cursor.execute(f"""SELECT name AS 'name', age AS 'age', city AS 'city' 
                       FROM {tables[table_number]} FOR JSON PATH;""")
            json_result = cursor.fetchone()[0]
            with open(f'{JSON_NAME}', 'w') as f:     #Create JSON file.
                json.dump(json.loads(json_result), f, indent=4)
                print(f"{JSON_NAME} file created successfully!")
    except pyodbc.Error as e:
        print(str(e))
        return None


#Close the connection with the Database.

def close_connection():
    cursor.close()
    connection.close()


#Call the functions. 

try:
    create_connection(SERVER, USERNAME, PASSWORD)       #Establish Connection
    create_database(DATABASE)                           #Create Database
    create_table(tables)                                #Create Tables
    populate_tables(names,ages,cities)                  #Populate Tables
    export_table()                                      #Export one of the Tables
except pyodbc.OperationalError as e:
    print("Could not establish connection: "+ str(e))
except pyodbc.Error as e:
    print("You have an error:", e)
finally:
    close_connection()                                  #Close Connection
    print("Connection closed: finally")








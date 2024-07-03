#Import Libraries 
import pyodbc, json, os, random
from os.path import exists
from credentials import SERVER, PASSWORD, USERNAME, DATABASE, JSON_NAME, NEW_USERNAME, NEW_PASSWORD, NEW_USER
# from variables import dict_tables
JSON_NAME="ExportJson.json"
# Additional varibles
dict_tables = {'First':['Alice',30,'New York'],'Second':['Bob', 25,'Los Angeles'], 'Third':['Charlie',22,'Chicago']}

#
# SERVER=".,1433"
# PASSWORD="Cirica01@@"
# USERNAME="sa"
# DATABASE="trydatabasebun"
# JSON_NAME="jdsdsantryfilebun.json"
# #
#
# SERVER=".,1433"
# NEW_PASSWORD='logincoco1234@@'
# NEW_USERNAME='login4'
# NEW_USER='userlogin4'
# # # DATABASE="login"


#Create the connection to SQL Server
def create_connection(server, username, password):
    global connection, cursor                          #Globally declared variables in order to use them in the next functions.
    connection_str = (
        f'DRIVER={{ODBC Driver 18 for SQL Server}};'
        f'SERVER={server};'
        f'UID={username};'
        f'PWD={password};'
        # f'DATABASE={DATABASE};'
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




# create_login()
def create_database(database=DATABASE):                     
    try:                                              #Creating the database and checks if the database already exists or not. 
        cursor.execute(f"""
                        BEGIN CREATE DATABASE {database}
                        END""")
        print("Database created.")
        cursor.execute(f"USE {database}")
        print(f"Using the {database} database.")
    except pyodbc.Error as e:
        if "42000" in str(e):
            print(f"Error '42000': Database '{database}' already exists")
            return None

#Create the tables.

def create_table():
    try:                                               #Creating the table and checks if the table already exists or not in the database.
        for table in dict_tables.keys():
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

def populate_tables():
    try:                                               #Populate the table with values from 3 lists(names, ages, cities).
        # Ensure the lists have the same length
        for key in dict_tables.keys():
            cursor.execute(f"""                                
                               INSERT INTO {key} (name, age, city) 
                               VALUES (?, ?, ?)
                               """, (dict_tables[key][0], dict_tables[key][1], dict_tables[key][2]))
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
            table_list = []
            export_list= []
            for table_key in dict_tables.keys():
                cursor.execute(f"SELECT name AS 'name', age AS 'age', city AS 'city' FROM {table_key} FOR JSON PATH;")
                json_result=cursor.fetchone()[0]
                table_list.append(json_result)
            for i in range(len(table_list)):
                export_list.append(json.loads(table_list[i])[0])
            with open(f'{JSON_NAME}', 'w') as f:     #Create JSON file.
                json.dump(export_list, f, indent=4)
                print(f"{JSON_NAME} file created successfully!")
    except pyodbc.Error as e:
        print(str(e))
        return None

#Create new login
def create_login():
    cursor.execute(f"CREATE LOGIN {NEW_USERNAME} WITH PASSWORD = '{NEW_PASSWORD}';");
    cursor.execute(f"CREATE USER {NEW_USER} FOR LOGIN {NEW_USERNAME}")
    cursor.execute(f"EXEC sp_addsrvrolemember '{NEW_USERNAME}', 'sysadmin';")
    cursor.execute(f"USE {DATABASE}")
    print("I`m using the new login")


#Close the connection with the Database.

def close_connection():
    cursor.close()
    connection.close()


#Call the functions. 

try:
    create_connection(SERVER, USERNAME, PASSWORD)       #Establish Connection
    create_database(DATABASE)                           #Create Database
    create_table()                                #Create Tables
    populate_tables()                  #Populate Tables
    create_login()
    create_connection(SERVER,NEW_USERNAME,NEW_PASSWORD)
    cursor.execute(f"USE {DATABASE}")
    export_table()                                      #Export one of the Tables
except pyodbc.OperationalError as e:
    print("Could not establish connection: "+ str(e))
except pyodbc.Error as e:
    print("You have an error:", e)
finally:
    close_connection()                                  #Close Connection
    print("Connection closed: finally")








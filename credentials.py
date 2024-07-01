import os

#Credentials Variables
SERVER=os.environ.get('HOST')
PASSWORD=os.environ.get('MSSQL_ROOT_PASSWORD')
USERNAME=os.environ.get("USER")
DATABASE=os.environ.get('DATABASE')
JSON_NAME=os.environ.get('JSON_NAME')

#Global Variables
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 22]
cities = ['New York', 'Los Angeles', 'Chicago']
tables = ['First','Second','Third']


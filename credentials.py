import os


SERVER=os.environ.get('HOST')
PASSWORD=os.environ.get('$(password)')
USERNAME=os.environ.get("USER")
DATABASE=os.environ.get('DATABASE')
TABLE=os.environ.get('TABLE')
JSON_NAME=os.environ.get('JSON_NAME')


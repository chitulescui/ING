import os
host = os.environ.get("HOST")
user = os.environ.get("USER")
password = os.environ.get('MSSQL_ROOT_PASSWORD')
sqlport = int(os.environ.get("SQLPORT"))
auth_plugin = os.environ.get("AUTH_PLUGIN")
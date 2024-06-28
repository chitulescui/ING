import os
host = os.environ.get("HOST")
user = os.environ.get("USER")
password = os.environ.get('MYSQL_ROOT_PASSWORD')
port = int(os.environ.get("PORT"))
auth_plugin = os.environ.get("AUTH_PLUGIN")
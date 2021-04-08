import mysql.connector

# MySQL Workbench data in order to connect

connection = mysql.connector.connect(
    host='localhost',       # MySql host name (example)
    user='root',            # MySql username (example)
    password='mysql1234',   # MySql password (example)
    database='example'      # Database name in MySql
)

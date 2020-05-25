# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='M2TVdyym3s', passwd='dllVFPIUdv', db='M2TVdyym3s')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM M2TVdyym3s.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

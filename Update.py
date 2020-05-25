# Establishing a connection to DB
import pymysql
conn = pymysql.connect(host='remotemysql.com', port=3306, user='M2TVdyym3s', passwd='dllVFPIUdv', db='M2TVdyym3s')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE M2TVdyym3s.users SET id = '10' WHERE name = 'john'")

cursor.close()
conn.close()

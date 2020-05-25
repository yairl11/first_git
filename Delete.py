# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='M2TVdyym3s', passwd='dllVFPIUdv', db='M2TVdyym3s')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM M2TVdyym3s.users WHERE name = 'john'")

cursor.close()
conn.close()

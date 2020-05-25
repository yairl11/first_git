# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='M2TVdyym3s', passwd='dllVFPIUdv', db='M2TVdyym3s')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into M2TVdyym3s.users (name, id) VALUES ('john', 5)")

cursor.close()
conn.close()

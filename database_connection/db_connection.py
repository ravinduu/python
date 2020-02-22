#install mysql connector > pip install mysql-connector
import mysql.connector as msq

db_conn = msq.connect(host = "localhost/ip",user = "user_name", passwd = "password",database = "database_name")
mycursor = db_conn.cursor()

mycursor.execute("query need to execute")
result = mycursor.fetchall()

for i in result:
	print(i)

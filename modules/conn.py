import mysql.connector as conn

db = conn.connect(
	host="localhost",
	user="root",
	password="root123",
)

cursor = db.cursor()

initial_query = open("database.sql").read()
cursor.execute(initial_query)
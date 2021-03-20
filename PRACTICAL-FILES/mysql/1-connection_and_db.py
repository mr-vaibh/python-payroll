import mysql.connector as conn

db = conn.connect(
	host="localhost",
	user="root",
	password="root123",
)

print(db)

# Creating DB
cursor = db.cursor()

cursor.execute("CREATE DATABASE good_database")

# Listing all DB(s)
cursor.execute("SHOW DATABASES")

for database in cursor:
	print(database)
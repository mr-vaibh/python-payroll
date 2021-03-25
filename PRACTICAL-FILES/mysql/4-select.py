import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root123",
	database="good_database"
)

cursor = db.cursor()

# `*` for displaying all columns
# cursor.execute("SELECT * FROM customers")
cursor.execute("SELECT name, address FROM customers")

record = cursor.fetchall()

for row in record:
	print(row)

print('\n')

# WHERE clause
query = "SELECT * FROM customers WHERE address ='Dwarka'"
cursor.execute(query)
record = cursor.fetchall()

for row in record:
  print(row)
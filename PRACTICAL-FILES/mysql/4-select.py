import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

cursor = db.cursor()

# `*` for displaying all columns
# cursor.execute("SELECT * FROM customers")
cursor.execute("SELECT name, address FROM customers")

record = cursor.fetchall()

for row in record:
    print(row)


# WHERE clause
query = "SELECT * FROM customers WHERE address ='Central st 954'"
cursor.execute(query)
record = cursor.fetchall()

for row in record:
  print(row)
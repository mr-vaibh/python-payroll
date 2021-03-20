import mysql.connector as conn

db = conn.connect(
	host="localhost",
	user="root",
	password="root123",
	database="good_database"
)
cursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)

# This commit method tells to SAVE the row in DB
db.commit()

print(cursor.rowcount, "record inserted.")


# Inserting many values
val = [
  ('Peter', 'Lowstreet 4'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val)
db.commit()
print(cursor.rowcount, "records inserted.")


# UPDATE
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Park Lane 38'"
cursor.execute(sql)
db.commit()

print(cursor.rowcount, "record(s) updated")
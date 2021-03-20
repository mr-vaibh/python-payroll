import mysql.connector as conn

db = conn.connect(
	host="localhost",
	user="root",
	password="root123",
	database="good_database"
)
cursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Vaibhav", "Dwarka 23B")
cursor.execute(sql, val)

# This commit method tells to SAVE the row in DB
db.commit()

print(cursor.rowcount, "record inserted.")


# Inserting many values
val = [
	('Aditya', 'Dwarka 21'),
	('Manas', 'Dwarka 23'),
	('Akhil', 'Samalka'),
	('Saurav', 'Bharthal'),
	('Sahil', 'Somewhere'),
	('RunningOutOfNames', 'Mind'),
	('God', 'Everywhere')
]

cursor.executemany(sql, val)
db.commit()
print(cursor.rowcount, "records inserted.")


# UPDATE
sql = "UPDATE customers SET address = 'Dwarka' WHERE address LIKE 'Dwarka%'"
cursor.execute(sql)
db.commit()

print(cursor.rowcount, "record(s) updated")
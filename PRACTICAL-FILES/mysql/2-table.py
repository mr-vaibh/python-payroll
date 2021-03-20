import mysql.connector as conn

db = conn.connect(
	host="localhost",
	user="root",
	password="root123",
	database="good_database",
)

cursor = db.cursor()

# Create Table
cursor.execute("CREATE TABLE customers (id INT, name VARCHAR(255), address VARCHAR(255))")

# Show all tables in `good_database`
cursor.execute("SHOW TABLES")

for table in cursor:
	print(table)

# Changing TABLE structure
cursor.execute("ALTER TABLE customers MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# cursor.execute("DROP TABLE IF EXISTS customers")
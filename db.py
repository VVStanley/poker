import sqlite3


connection = sqlite3.connect("tutorial.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data (
ID varchar(255) NOT NULL UNIQUE,
HEX varchar(255) NOT NULL UNIQUE,
CARDS varchar(255) NOT NULL UNIQUE
)""")

result = cursor.execute("""SELECT count(*) FROM data""")
amount = result.fetchall()[0]
print(amount)

connection.commit()
connection.close()

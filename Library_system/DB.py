import sqlite3 as sql

connection = sql.connect("Students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    book TEXT,
    date TEXT,
    delivery TEXT
)
""")


cursor.execute("SELECT * FROM users")
datas = cursor.fetchall()
connection.commit()

print(datas)
connection.close()

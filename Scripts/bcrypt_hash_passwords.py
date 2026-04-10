import sqlite3
import bcrypt

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT username, password FROM users")

for row in cursor.fetchall():
    username = row[0]
    password = row[1].encode()

    # Generate bcrypt hash
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    print(username + ":" + hashed.decode())

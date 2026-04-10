import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT username,password FROM users")

for row in cursor.fetchall():
    username = row[0]
    password = row[1]

    hashed = hashlib.sha256(password.encode()).hexdigest()

    print(username + ":" + hashed)

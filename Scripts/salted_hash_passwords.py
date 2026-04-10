import sqlite3
import hashlib
import os

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT username, password FROM users")

for row in cursor.fetchall():
    username = row[0]
    password = row[1]

    # Generate random salt
    salt = os.urandom(16).hex()

    # Create salted hash
    salted_password = salt + password
    hashed = hashlib.sha256(salted_password.encode()).hexdigest()

    print(username + ":" + salt + ":" + hashed)


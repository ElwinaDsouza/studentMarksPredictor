import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()
c.execute("SELECT * FROM students")
print("Connecting to database...")

c.execute("SELECT * FROM students")
rows = c.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No predictions found. Make some predictions first!")


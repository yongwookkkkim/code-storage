import sqlite3

conn=sqlite3.connect('database.db')
c=conn.cursor()

c.execute("SELECT * FROM database")

for item in c.fetchall():
    print(item)

conn.commit()
conn.close()
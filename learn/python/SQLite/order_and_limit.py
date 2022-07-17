import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")
#DROP TABLE customers -> this deletes the table 

for item in c.fetchall():
    print(item)

conn.commit()
conn.close()
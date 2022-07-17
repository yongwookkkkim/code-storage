import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()

c.execute("DELETE from customers WHERE rowid=6")

conn.commit()

c.execute("SELECT * from customers")

for item in c.fetchall():
    print(item)

conn.close()
import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()

c.execute("SELECT * FROM customers")
#c.fetchone()[0]->return the first element of the tuple
#c.fetchmany(3)
items=c.fetchall()
for item in items:
    print(item[0])

conn.commit()
conn.close()
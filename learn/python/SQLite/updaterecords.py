import sqlite3

conn=sqlite3.connect('customer.db')
c=conn.cursor()

c.execute("""
    UPDATE customers SET first_name='Marty'
    WHERE rowid=3
""")

conn.commit()

c.execute("SELECT rowid,* FROM customers")

for item in c.fetchall():
    print(item)

conn.close()
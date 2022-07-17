import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()

#c.execute("SELECT * FROM customers WHERE last_name='Elder'")
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'") #this is also possible

print(c.fetchall())

conn.commit()
conn.close()
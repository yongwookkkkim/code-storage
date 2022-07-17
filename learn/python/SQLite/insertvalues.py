import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()

#insert many records
many_customer=[
    ('Wes', 'Brown', 'wes@brown.com'),
    ('Steph', 'Kuewa', 'steph@kuewa.com'),
    ('Dan', 'Pas', 'dan@pas.com')
    ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer) #?,?,? for first_name, last_name, email

#insert single record
#c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

conn.commit()
conn.close()
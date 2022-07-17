import sqlite3

#connect to a database
conn=sqlite3.connect('customer.db')

#create a cursor
c=conn.cursor()

#create a table
c.execute(""" CREATE TABLE customers(
    first_name text,
    last_name text,
    email text
)""")

#DATATYPEs
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#commit the command
conn.commit()

#close the connection
conn.close()
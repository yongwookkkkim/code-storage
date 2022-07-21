import random
import sqlite3

#basic functions
def login(accno, pw):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute(f"SELECT rowid, * FROM database WHERE account_no={accno}")
    found=c.fetchone()
    conn.commit()
    conn.close()
    return found[0]

def createacc(accno,pw, fname, sname):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("INSERT INTO database VALUES (?,?,?,?,?)", (accno, pw, fname, sname, 0.0))
    conn.commit()
    conn.close()

def createaccno():
    sameaccno=True
    accno=''
    while sameaccno:
        accno=''
        for i in range(8):
            accno+=str(random.randint(1,9))
        accno=int(accno)
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        c.execute(f"SELECT * FROM database WHERE account_no={accno}")
        if len(c.fetchall())==0:
            sameaccno=False
    return accno

def addval(id,increment):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute(f"SELECT balance FROM database WHERE rowid={id}")
    currentbal=c.fetchone()[0]
    c.execute(f"UPDATE database SET balance={currentbal+increment}")
    conn.commit()
    conn.close()

def withdraw(id, decrement):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute(f"SELECT balance FROM database WHERE rowid={id}")
    currentbal=c.fetchone()[0]
    c.execute(f"UPDATE database SET balance={currentbal-decrement}")
    conn.commit()
    conn.close()

def checkbal(id):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute(f"SELECT balance FROM database WHERE rowid={id}")
    currentbal=c.fetchone()[0]
    conn.commit()
    conn.close()
    return currentbal

def noservice():
    print("We provide no such service.")
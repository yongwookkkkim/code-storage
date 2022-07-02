import pandas as pd
import numpy as np
import random

#read excel
location='./projects/atm/database.xlsx'
df=pd.read_excel(location)

#rename columns and rows
df.index=['accno', 'fname', 'sname', 'pw', 'bal', 'hist']
df.columns=np.array(df.loc['accno'])
print(df.dtypes  )

#basic functions
def login():
    wrongcount=0
    accno=int(input("Enter your account number: "))
    while accno not in df.columns:
        accno=int(input("Enter your account number: "))
    pw=input("Enter your password: ")
    if pw==df.loc['pw', accno]:
        return True
    else:
        return False

def createacc():
    fname=input("Enter your first name: ")
    sname=input("Enter your surname: ")
    pw=input("Enter your password: ")
    pwcheck=input("Enter your password again: ")
    if pw!=pwcheck:
        print("The passwords don't match.")
        return False
    else:
        bal=1000
        accno='0'
        print(df.loc['accno'])
        while int(accno) not in df.loc['accno']:
            accno=''
            for i in range(8):
                accno+=str(random.randint(1,9))
            df[accno]=[accno, fname, sname, pw, bal, 'none']
        print("Account successfully created.")

def addval():
    pass

def withdraw():
    pass

def checkbal():
    pass

def checkhist():
    pass

def noservice():
    print("We provide no such service.")

def run():
    on=True
    while on:
        login()
        op=input("What service do you seek: ")
        if op=='0':
            createacc()
        on=False
        print(df)

if __name__=='__main__':
    run()
    pass
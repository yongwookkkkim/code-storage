import pandas as pd
import random

data=pd.read_excel(r'./projects/atm/database.xlsx')
df=pd.DataFrame(data)

class account():
    def __init__(self, fname, sname, pw, accno, bal=100, hist=[]):
        self.fname=fname
        self.sname=sname
        self.bal=bal
        self.hist=hist
        self.pw=pw
        #create random accno


'''
def createacc():
    #basic info
    fname=input("Enter your first name: ")
    sname=input("Enter your surname: ")
    #creating a valid password
    corrpw=False
    while not corrpw:
        pw=input("Enter your password: ")
        pwcheck=input("Enter your password again: ")
        if pw==pwcheck:
            corrpw=True
        else:
            print("Two passwords are different.")
    #creating a unique accno
    acno=df.loc[0,'last_no']
    df.loc[0,'last_no']=acno+=1
    newacc=account(fname, sname, pw, acno)
    
run=True
while run:
    print("hi")    

df.to_excel('./projects/atm/database.xlsx')
'''
print(df.loc[0,1])
import sqlite3
import functions as fn

def printui():
    print('')
    print('')
    print("Yongwook's ATM")
    print("----------------------------------------")
    print("To create a new account, press '1'")
    print("To add balance, press '2'")
    print("To withdraw, press '3'")
    print("To check balance, press '4'")
    print("To terminate, press 't'")
    print("----------------------------------------")

def createnewacc():
    fname=input("Enter your first name: ")
    sname=input("Enter your surname: ")
    corrpw=False
    for i in range(3):
        pw=input("Enter your password: ")
        pwconfirm=input("Confirm your password: ")
        if pw==pwconfirm:
            corrpw=True
            break
        else:
            print(f"The passwords don't match. You have {2-i} chance(s) remaining to enter a correct password")
    if corrpw:
        accno=fn.createaccno()
        fn.createacc(accno,pw,fname,sname)
        print(f"Account successfully created! Your account number is {accno}")
    else:
        print("Failed to create an account.")

def addbal():
    try:
        accno=float(input("Enter your account number: "))
    except ValueError:
        print("Wrong account number")
    pw=input("Enter your password: ")
    id=fn.login(accno,pw)
    inc=int(input("How much would you like to add: "))
    fn.addval(id, inc)
    print(f"${inc} successfully added. Your current balance is £{fn.checkbal(id)}")

def withdr():
    try:
        accno=float(input("Enter your account number: "))
    except ValueError:
        print("Wrong account number")
    pw=input("Enter your password: ")
    id=fn.login(accno,pw)
    dec=int(input("How much would you like to withdraw: "))
    fn.withdraw(id, dec)
    print(f"£{dec} successfully withdrawn. Your current balance is £{fn.checkbal(id)}")

def checkbalance():
    try:
        accno=int(input("Enter your account number: "))
    except ValueError:
        print("Wrong account number")
    pw=input("Enter your password: ")
    id=fn.login(accno,pw)
    print(f"Your current balance is £{fn.checkbal(id)}")

def noservice():
    print("We provide no such service.")

servicefunc={
    '1':createnewacc,
    '2':addbal,
    '3':withdr,
    '4':checkbalance
}

def run():
    on=True
    while on:
        printui()
        service=input("What service do you seek: ")
        if service=='t':
            break
        else:
            servicefunc.get(service, noservice)()
    print("----------------------------------------")
    print("Thank you for using us. Have a great day!")

run()
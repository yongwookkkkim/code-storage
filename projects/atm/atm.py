import random

def createAccountNo():
    accountNo=0
    for i in range(8):
        accountNo += random.randrange(1,10)*(10**i)
    return accountNo

class account():
    def __init__(self, firstname, surname, balance, history, password, accountnoinput=1):
        self.firstname = firstname
        self.surname = surname
        self.balance = balance
        self.history = history
        self.password=password
        if accountnoinput==1:
            repeat=True
            while repeat:
                accountNo=createAccountNo()
                overlap=False
                for account in database:
                    if account.accountNo==accountNo:
                        overlap=True
                if overlap==False:
                    self.accountNo=accountNo
                    repeat=False
        else:
            self.accountNo=accountnoinput
    
    def passwordcheck(self):
        correctPassword=False
        wrongcount=0
        while (not correctPassword )and wrongcount<=3:
            passwordInput = input("Enter your password: ")
            if passwordInput == self.password:
                correctPassword=True
            else:
                print(f"Wrong password. You have {3-wrongcount} attempts remaining.\n")
                wrongcount+=1
        return correctPassword
     
def identification():
    accountNoInput = input("Please enter your account no: ")
    res=0
    for account in database:
        if accountNoInput==account.accountNo:
            res = database.index(account)
            break
    a=database[res].passwordcheck()
    if a==True:
        return res
    else: 
        return 0


def createNewAccount():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    balance=100
    history=[]
    correctPassword = False
    while not correctPassword:
        password1 = input("Please enter a password: ")
        password2 = input("Confirm password: ")
        if password1==password2:
            correctPassword=True
            break
        else:
            print("The passwords don't match.\n")   
    accountCreated=account(firstname, lastname, balance, history, password1)
    database.append(accountCreated)
    appendDatabase(accountCreated)
    print(f"Your Account Number is {accountCreated.accountNo}")
    
def checkBalance():
    accountAccess=identification()
    print(f"Your balance is {database[accountAccess].balance}")

def cashWithdrawal():
    accountAccess = identification()
    account = database[accountAccess]
    withdrawalAmount = int(input("How much would you like to withdraw: "))
    if withdrawalAmount <= account.balance:
        account.balance -= withdrawalAmount
        print(f"You withdrew {withdrawalAmount}, Balance: {account.balance}")
    else:
        print(f"That exceeds your balance. Your current balance is {account.balance}\n")
    account.history.append("w"+str(withdrawalAmount))

def addValue():
    accountAccess = identification()
    account = database[accountAccess]
    additionAmount = int(input("How much would you like to add: "))
    account.balance += additionAmount
    print(f"You added {additionAmount}, Balance: {account.balance}")
    account.history.append("a"+str(additionAmount))

def seeHistory():
    accountAccess = identification()
    account = database[accountAccess]
    print("-Your Account's History-")
    for item in account.history:
        if item.startswith("a"):
            print(f"Added: "+item.replace('a',''))
        elif item.startswith("w"):
            print(f"Withdrew: "+item.replace('w',''))

def appendDatabase(accIn):
    history=";".join([item for item in accIn.history])
    baseAppend.write("\n"+ accIn.firstname)
    baseAppend.write("\n"+ accIn.surname)
    baseAppend.write("\n"+ str(accIn.balance))
    baseAppend.write("\n"+ history)
    baseAppend.write("\n"+ accIn.password)
    baseAppend.write("\n"+ str(accIn.accountNo))

power = True
read = open('projects/atm/database.txt','r')
baseAppend=open('projects/atm/database.txt', 'a')
baseRead=read.read()
database=[]
baseReadLineSplit = baseRead.split("\n")
j=0
for i in range(len(baseReadLineSplit)):
    if i%6==0:
        firstnameRead=baseReadLineSplit[i]
        j+=1
    elif i%6==1:
        surnameRead=baseReadLineSplit[i]
        j+=1
    elif i%6==2:
        balanceRead=int(baseReadLineSplit[i])
        j+=1
    elif i%6==3:
        historyRead=baseReadLineSplit[i].split(";")
        j+=1
    elif i%6==4:
        passwordRead=baseReadLineSplit[i]
        j+=1
    elif i%6==5:
        accountNoRead=int(baseReadLineSplit[i])
        j+=1
    if j==6:
        database.append(account(firstnameRead,surnameRead,balanceRead,historyRead,passwordRead,accountNoRead))
        j=0

#main loop
while(power):
    service = input("\n<possible services>\ncreate new account (press 0)\ncheck balance (press 1)\ncash withdrawal (press 2)\nadd value (press 3)\nsee history (press 4)\nterminate service (press t)\n\nWhich service do you seek: ")
    print("")
    if service=="0":
        createNewAccount()
    elif service=="1":
        checkBalance()
    elif service=="2":
        cashWithdrawal()
    elif service=="3":
        addValue()
    elif service=="4":
        seeHistory()
    elif service=="t":
        power=False
    else:
        print("We provide no such service.\n")
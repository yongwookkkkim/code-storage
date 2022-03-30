import random

power = True
base = open('scripts/database.txt', 'r')

database = []

def createAccountNo():
    accountNo=0
    for i in range(8):
        accountNo += random.randrange(1,10)*(10**i)
    return accountNo

class account():
    def __init__(self, firstname, lastname, balance, history, password):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.history = history
        self.password=password
        repeat=True
        overlap=False
        accountNo=0
        while repeat:
            if len(database)!=0:
                accountNo=createAccountNo()
                overlap=False
                for account in database:
                    if account.accountNo==accountNo:
                        overlap=True
                if overlap==False:
                    self.accountNo=accountNo
                    repeat=False       
            else:
                self.accountNo=11111111 
                repeat=False
    
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
    print(f"Your Account Number is {accountCreated.accountNo}")
    
def checkBalance():
    accountAccess=identification()
    print(database[accountAccess].balance)

def cashWithdrawal():
    accountAccess = identification()
    account = database[accountAccess]
    withdrawalAmount = int(input("How much would you like to withdraw: "))
    if withdrawalAmount <= account.balance:
        account.balance -= withdrawalAmount
        print(f"You withdrew {withdrawalAmount}, remainder: {account.balance}")
    else:
        print(f"That exceeds your balance. Your current balance is {account.balance}\n")
    account.history.append("Withdrew: " + str(withdrawalAmount) + ", Balance: " + str(account.balance))

def addValue():
    accountAccess = identification()
    account = database[accountAccess]
    additionAmount = int(input("How much would you like to add: "))
    account.balance += additionAmount
    print(f"You added {additionAmount}, Balance: {account.balance}")
    account.history.append("Added: " + str(additionAmount) + ", Balance: " + str(account.balance))

def seeHistory():
    accountAccess = identification()
    account = database[accountAccess]
    print("-Your Account's History-")
    for item in account.history:
        print(item + "\n")

while(power):
    service = input("\n<possible services>\ncreate new account (press 0)\ncheck balance (press 1)\ncash withdrawal (press 2)\nadd value (press 3)\nsee history (press 4)\nterminate service (press t)\n\nWhat service do you seek: ")
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
#!/usr/bin/python


class Account:
    def __init__(self, acctNumber, balance):
        self.acctNumber = acctNumber
        self.balance = balance

    def __str__(self):
        return 'Account number: ' + str(self.acctNumber) + '\n' +\
               'Balance: ' + str(self.balance)

    def deposit(self, amount):
        self.balance += amount


class Checking(Account):
    def __init__(self, acctNumber, balance, fee):
        Account.__init__(self, acctNumber, balance)
        self.fee = fee

    def __str__(self):
        reStr = 'Account type: Checking\n'
        reStr += Account.__str__(self)
        return reStr

    def getFee(self):
        return self.fee

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount - self.fee


class Savings(Account):
    def __init__(self, acctNumber, balance):
        Account.__init__(self, acctNumber, balance)

    def __str__(self):
        retStr = 'Account type: Savings\n'
        retStr += Account.__str__(self)
        return retStr

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount


ca = Checking("12345", 500, .50)
print(ca)
ca.withdraw(100)
print(ca)
ca.deposit(200)
print(ca)

print('')
sa = Savings('456789', 1000.0)
print(sa)
sa.withdraw(250)
print(sa)
sa.deposit(125)
print(sa)

print('')
accounts = [ca, sa]
print("Display all account: ")
for i in range(0, len(accounts)):
    print(accounts[i])
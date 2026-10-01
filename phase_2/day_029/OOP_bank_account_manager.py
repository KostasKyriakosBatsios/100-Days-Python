# Day 29 1/10/26

import re

PATTERN_NAME = r"[A-Za-z\s]+"

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def display(self):
        print(f"\nAccount: {self.account_number}\nOwner: {self.owner}\nBalance: {self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = []
    
    def show_accounts(self):
        length = update_length(self.accounts)
        if length == 0:
            print("No accounts were found!")
            return 0
        
        for i in range(length):
            self.accounts[i].display()
    
    def add_account(self):
        an, o, b = 0, "", 0
        
        while an <= 0:
            try:
                an = int(input("Account number: "))
                for i in range(len(self.accounts)):
                    if an == self.accounts[i].account_number:
                        print("An account with that number already exists!")
                        an = 0
                        break
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_NAME, o): o = input("Owner: ")
        
        while b <= 0:
            try:
                b = float(input("Balance: "))
            except ValueError:
                continue
        
        temp = BankAccount(an, o, b)
        self.accounts.append(temp)
    
    def find_account(self, account_number):
        length = update_length(self.accounts)
        flag = False
        
        for i in range(length):
            if account_number == self.accounts[i].account_number:
                self.accounts[i].display()
                flag = True
        
        if not flag:
            print(f"No account {account_number} was found!")
            return 0
    
    def deposit_to_account(self):
        length = update_length(self.accounts)
        if length == 0:
            print("No accounts were found!")
            return 0
        an, pos, am = 0, 0, 0
        
        while True:
            try:
                an = int(input("Account number: "))
                if an <= 0:
                    continue
                
                flag = False
                
                for i in range(length):
                    if an == self.accounts[i].account_number:
                        pos = i
                        flag = True
                        break
                
                if flag:
                    break
            except ValueError:
                continue
        
        while am <= 0:
            try:
                am = float(input("Amount: "))
            except ValueError:
                continue
        
        self.accounts[pos].deposit(am)
    
    def withdraw_from_account(self):
        length = update_length(self.accounts)
        if length == 0:
            print("No accounts were found!")
            return 0
        an, pos, am = 0, 0, 0
        
        while True:
            try:
                an = int(input("Account number: "))
                if an <= 0:
                    continue
                
                flag = False
                
                for i in range(length):
                    if an == self.accounts[i].account_number:
                        pos = i
                        flag = True
                        break
                
                if flag:
                    break
            except ValueError:
                continue
        
        while am <= 0:
            try:
                am = float(input("Amount: "))
                if am > self.accounts[pos].balance:
                    print("The number cannot be larger than the total amount.")
                    continue
            except ValueError:
                continue
        
        self.accounts[pos].withdraw(am)

def main():
    print("======== BANK MANAGEMENT SYSTEM ========")
    bank = Bank()
    
    while True:
        num = get_int("\n1. Show all accounts\n2. Create account\n3. Find account\n4. Deposit\n5. Withdraw\n6. Exit\n\nChoose: ")
        match(num):
            case 1: bank.show_accounts()
            case 2: bank.add_account()
            case 3:
                length = update_length(bank.accounts)
                n = get_number(length)
                if n != 0:
                    bank.find_account(n)
            case 4: bank.deposit_to_account()
            case 5: bank.withdraw_from_account()
            case 6: break
    
    print("Goodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            if not (1 <= n <= 6):
                continue
            break
        except ValueError:
            continue
    
    return n

def update_length(a):
    return len(a)

def get_number(size):
    if size == 0:
        print("No accounts were found.")
        return 0
                
    n = 0
                
    while n <= 0:
        try:
            n = int(input("Search for account number: "))
        except ValueError:
            continue
    
    return n

main()

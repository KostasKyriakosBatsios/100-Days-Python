# Day 54 2/11/26

class BankAccount:
  def __init__(self, account_id, owner, balance):
    self.account_id = account_id
    self.owner = owner
    self.balance = balance
    self.transactions = []
    
    
  def deposit(self, amount):
    if amount <= 0:
      return False
      
    self.balance += amount
    self.transactions.append(f"Deposit: {amount}€")
    return True
      
    
  def withdraw(self, amount):
    if amount <= 0 or amount > self.balance:
      return False
      
    self.balance -= amount
    self.transactions.append(f"Withdrawal: -{amount}€")
    return True
      
    
  def display_balance(self):
    print(f"\nBalance: {self.balance}")
    
    
  def display_transactions(self):
    if self.transactions:
      print("Transactions:")
      for t in self.transactions:
        print(t)
    else:
      print("\nTransactions: []")


class Bank:
  def __init__(self):
    self.bank_accounts = []
    
    
  def create_account(self):
    a_id, o, b = 1, "", 0.0
    existing_ids = [a.account_id for a in self.bank_accounts]
        
    while a_id in existing_ids:
      a_id += 1
  
    while not o:
      o = input("\nOwner: ")
            
      if any((c.isdigit() or c in ["'", "?", "!", ","]) for c in o):
        print("\nOnly characters!")
        o = ""
        
    while True:
      try:
        b = float(input("\nBalance: "))
      except ValueError:
        print("\nOnly numbers!")
        continue
        
      if b >= 0.0:
        break
                
      print("\nOnly non negative numbers!")
        
    self.bank_accounts.append(BankAccount(a_id, o, b))
    print("\nNew account was created successfully!")
        
    
  def search_account(self, account_id):
    if not self.bank_accounts:
      return print("\nNo bank accounts were found!")
        
    flag = False
        
    for a in self.bank_accounts:
      if account_id == a.account_id:
        flag = True
        print(f"\nAccount ID: {a.account_id}\nOwner: {a.owner}")
        a.display_balance()
        a.display_transactions()
        
    if not flag:
      print(f"\nNo account with ID {account_id} was found!")
    
    
  def delete_account(self, account_id):
    if not self.bank_accounts:
      return print("\nNo bank accounts were found!")
      
    pos, flag = 0, False
    
    for i, a in enumerate(self.bank_accounts):
      if account_id == a.account_id:
        pos, flag = i, True

    if flag:
      ch = ''

      while ch not in ['y', 'n']:
        ch = input("\nAre you sure? [y/n]\n- ").lower()

      if ch == 'n':
        return print("\nAccount will not be deleted!")

      self.bank_accounts.pop(pos)
      print("\nAccount was deleted successfully!")
    else:
      print(f"\nNo account with ID {account_id} was found!")
        
    
  def display_accounts(self):
    if not self.bank_accounts:
      return print("\nNo bank accounts were found!")
        
    for a in self.bank_accounts:
      print(f"\nAccount ID: {a.account_id}\nOwner: {a.owner}")
      a.display_balance()
      a.display_transactions()
    
    
  def transfer_money(self):
    if not self.bank_accounts:
      return print("\nNo bank accounts were found!")

    transmitter_id, receiver_id = 0, 0
    pos_t, pos_r = 0, 0
    flag_first_id = False

    while True:
      try:
        transmitter_id = int(input("\nAccount ID (will send money): "))
      except ValueError:
        print("\nOnly numbers!")
        continue

      if transmitter_id > 0:
        break

      print("\nOnly positive numbers!")

    for i, a in enumerate(self.bank_accounts):
      if transmitter_id == a.account_id:
        pos_t = i
        flag_first_id = True

    if flag_first_id:
      flag_second_id = False
      
      while True:
        try:
          receiver_id = int(input("\nAccount ID (will receive money): "))
        except ValueError:
          print("\nOnly numbers!")
          continue

        if receiver_id > 0:
          break

        print("\nOnly positive numbers!")

      for i, a in enumerate(self.bank_accounts):
        if receiver_id == a.account_id:
          pos_r = i
          flag_second_id = True

      if flag_second_id:
        if transmitter_id != receiver_id:
          a = 0.0

          while True:
            try:
              a = float(input("\nAmount for transfer: "))
            except ValueError:
              print("\nOnly positive numbers!")
              continue

            if 0.0 < a <= self.bank_accounts[pos_t].balance:
              break

            print("\nAmount must be positive and not bigger than the available balance!")

          transmitter = self.bank_accounts[pos_t]
          receiver = self.bank_accounts[pos_r]

          if transmitter.withdraw(a):
            receiver.deposit(a)
            self.bank_accounts[pos_t].transactions.append(f"Transfer sent to account with ID {receiver_id}: -{a}€")
            self.bank_accounts[pos_r].transactions.append(f"Transfer received from account with ID {transmitter_id}: {a}€")
            print("\nThe transfer was successful!")
          else:
            print("\nTransfer failed!")
            
        else:
          print("\nThe IDs must be different!")
          
      else:
        print(f"\nAccount receiver with ID {receiver_id} was not found!")
        
    else:
      print(f"\nAccount transmitter with ID {transmitter_id} was not found!")


def main():
  print("===== BANK MANAGEMENT SYSTEM =====")  
  obj = Bank()
    
  while True:
    num = get_num("\n1. Create Account\n2. Display Accounts\n3. Search Account\n4. Deposit\n5. Withdraw\n6. Transfer Money\n7. Delete Account\n8. Exit\n\nChoose an option: ")
        
    match(num):
      case 1:
        obj.create_account()
      case 2:
        obj.display_accounts()
      case 3:
        n = 0
                
        while True:
          try:
            n = int(input("\nAccount ID: "))
          except ValueError:
            print("\nOnly numbers!")
            continue
                    
          if n > 0:
            break
                        
          print("\nOnly positive numbers")
                
        obj.search_account(n)
      case 4:
        a_id, a, pos, flag_id, flag_a = 0, 0.0, 0, False, False

        while True:
          try:
            a_id = int(input("\nAccount ID: "))
          except ValueError:
            print("\nOnly numbers!")
            continue

          if a_id > 0:
            break

          print("\nOnly positive numbers!")

        for i, a in enumerate(obj.bank_accounts):
          if a_id == a.account_id:
            pos, flag_id = i, True
            
            while True:
              try:
                a = float(input("\nAmount: "))
              except ValueError:
                print("\nOnly numbers")
                continue

              if a > 0.0:
                flag_a = True
                break

              print("\nOnly positive numbers!")

            if flag_a:
              break

        if flag_id:
          flag_deposit = obj.bank_accounts[pos].deposit(a)
          
          if flag_deposit:
            print("\nDeposit was successful!")
          else:
            print("\nAmount must be positive!")
            
        else:
          print(f"\nNo account with ID {a_id} was found")
      case 5:
        a_id, a, pos, flag_id, flag_a = 0, 0.0, 0, False, False

        while True:
          try:
            a_id = int(input("\nAccount ID: "))
          except ValueError:
            print("\nOnly numbers!")
            continue

          if a_id > 0:
            break

          print("\nOnly positive numbers!")

        for i, a in enumerate(obj.bank_accounts):
          if a_id == a.account_id:
            pos, flag_id = i, True
            
            while True:
              try:
                a = float(input("\nAmount: "))
              except ValueError:
                print("\nOnly numbers")
                continue

              if a > 0.0:
                flag_a = True
                break

              print("\nOnly positive numbers!")

            if flag_a:
              break

        if flag_id:
          flag_withdraw = obj.bank_accounts[pos].withdraw(a)
          
          if flag_withdraw:
            print("\nWithdrawal was successful!")
          else:
            print("\nThe amount must be positive and/or cannot be bigger than the available balance")
        else:
          print(f"\nNo account with ID {a_id} was found")
      case 6:
        obj.transfer_money()
      case 7:
        n = 0
                
        while True:
          try:
            n = int(input("\nAccount ID: "))
          except ValueError:
            print("\nOnly numbers!")
            continue
                    
          if n > 0:
            break
                        
          print("\nOnly positive numbers")
                
        obj.delete_account(n)
      case 8:
        break
    
  print("\nGoodbye!")


def get_num(p):
  while True:
    try:
      n = int(input(p))
    except ValueError:
      print("\nOnly numbers!")
      continue

    if 1 <= n <= 8:
      return n

    print("\nOnly positive numbers between 1 and 8!")


main()

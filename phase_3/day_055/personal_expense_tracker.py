# Day 55 4/11/26

import datetime as dt
import json

class Expense:
  def __init__(self, expense_id, description, category, amount, date):
    self.expense_id = expense_id
    self.description = description
    self.category = category
    self.amount = amount
    self.date = date


  def display_expense(self):
    print(f"\nExpense ID: {self.expense_id}\nDescription: {self.description}\nCategory: {self.category}\nAmount: {self.amount}€\nDate: {self.date}")


class ExpenseTracker:
  def __init__(self):
    self.expenses = []


  def add_expense(self):
    e_id, des, c, a, d = 1, "", "", 0.0, ""
    ids = [e.expense_id for e in self.expenses]

    while e_id in ids:
      e_id += 1

    while not des.strip():
      des = input("\nDescription: ")

      if des.isdigit():
        print("\nOnly characters!")
        des = ""

    while True:
      c = input("\nCategory: ").capitalize()

      if c in ["Food", "Transportation", "Entertainment", "Health", "Education", "Bills", "Other"]:
        break

      print("\nThe expense must belong to one of the following categories: Food, Transportation, Entertainment, Health, Education, Bills, Other,")

    while True:
      try:
        a = float(input("\nAmount: "))
      except ValueError:
        print("\nOnly numbers!")
        continue

      if a > 0.0:
        break

      print("\nOnly positive numbers!")

    while True:
      d = input("\nDate (dd-mm-YYYY): ")

      try:
        d = dt.datetime.strptime(d, "%d-%m-%Y")
        break
      except ValueError:
        print("\nOnly valid format on the date!")

    self.expenses.append(Expense(e_id, des, c, a, d))
    print("\nExpense added successfully!")
  
  
  def display_expenses(self):
    if not self.expenses:
      return print("\nNo expenses were found!")

    for e in self.expenses:
      e.display_expense()


  def search_expense(self):
    if not self.expenses:
      return print("\nNo expenses were found!")

    e_id, flag = 0, False

    while True:
      try:
        e_id = int(input("\nExpense ID: "))
      except ValueError:
        print("\nOnly numbers!")
        continue

      if e_id > 0:
        break

      print("\nOnly positive integers!")

    for e in self.expenses:
      if e_id == e.expense_id:
        flag = True
        e.display_expense()

    if not flag:
      print(f"No expense with ID {e_id} was found!")


  def delete_expense(self):
    if not self.expenses:
      return print("\nNo expenses were found!")

    e_id, flag = 0, False

    while True:
      try:
        e_id = int(input("\nExpense ID: "))
      except ValueError:
        print("\nOnly numbers!")
        continue

      if e_id > 0:
        break

      print("\nOnly positive integers!")

    for e in self.expenses:
      if e_id == e.expense_id:
        flag, ch = True, ''

        while ch not in ['y', 'n']:
          ch = input("\nAre you sure? [y/n]\n- ").lower()

        if ch == 'n':
          return print("\nOK. This expense will not be deleted!")

        self.expenses.remove(e)
        return print("\nThis expense was deleted successfully!")

    if not flag:
      print(f"\nNo expense with ID {e_id} was found!")


  def total_expenses(self):
    if not self.expenses:
      return print("\nNo expenses were found!")

    total = 0.0

    for e in self.expenses:
      total += e.amount
    
    print(f"\nTotal expenses: {total}€")


  def category_summary(self):
    if not self.expenses:
      return print("\nNo expenses were found!")

    temp = {}

    for e in self.expenses:
      if e.category not in temp:
        temp[e.category] = e.amount
      else:
        temp[e.category] += e.amount

    for k, v in temp.items():
      print(f"{k}: {v}€")


  def monthly_summary(self):
    if not self.expenses:
      return print("\nNo expenses were found!")

    temp = {}
    
    for e in self.expenses:
      m = e.date.strftime("%B %Y")

      if m not in temp:
        temp[m] = e.amount
      else:
        temp[m] += e.amount

    for k, v in temp.items():
      print(f"{k}: {v}€")


  def save_to_file(self):
    data, temp = [], {}
    
    for e in self.expenses:
      temp = vars(e).copy()
      temp['date'] = e.date.strftime("%d-%m-%Y")
      data.append(temp)
    
    with open('phase_3/day_055/expenses.json', 'w') as f:
      json.dump(data, f, indent=4)

    print("\nThe expenses were saved!")


  def load_from_file(self):
    try:
      with open('phase_3/day_055/expenses.json', 'r') as f:
        self.expenses = json.load(f)
    except FileNotFoundError:
      return print("\nNo such file!")

    data, temp = [], {}
    
    for e in self.expenses:
      temp = e.copy()
      temp['date'] = dt.datetime.strptime(e['date'], "%d-%m-%Y")
      data.append(temp)
      
    new_list = []

    for d in data:
      obj = Expense(d['expense_id'], d['description'], d['category'], d['amount'], d['date'])
      new_list.append(obj)

    self.expenses = new_list
    print("\nThe file was loaded!")


def main():
  print("===== PERSONAL EXPENSE TRACKER =====")
  obj = ExpenseTracker()
  
  while True:
    num = get_num("\n1. Add Expense\n2. Display Expenses\n3. Search Expense\n4. Delete Expense\n5. Total Expenses\n6. Category Summary\n7. Monthly Summary\n8. Save Expenses\n9. Load Expenses\n10. Exit\n\nChoose an option: ")

    match num:
      case 1:
        obj.add_expense()
      case 2:
        obj.display_expenses()
      case 3:
        obj.search_expense()
      case 4:
        obj.delete_expense()
      case 5:
        obj.total_expenses()
      case 6:
        obj.category_summary()
      case 7:
        obj.monthly_summary()
      case 8:
        obj.save_to_file()
      case 9:
        obj.load_from_file()
      case _:
        break

  print("\nGoodbye!")


def get_num(p):
  while True:
    try:
      n = int(input(p))
    except ValueError:
      print("\nOnly numbers!")
      continue
      
    if 1 <= n <= 10:
      return n

    print("\nOnly integers between 1 and 10!")


main()

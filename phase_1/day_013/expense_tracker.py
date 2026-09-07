import re

PATTERN_INPUT = r"[A-Za-z]+"
PATTERN_AMOUNT = r"^\d+\.\d{1,2}$"


def main():
  print("=== Expense Tracker ===")
  expenses = []
  choice = 0
  while choice != 5:
    choice = get_number("\n1. Add expense\n2. View all expenses\n3. View total expenses\n4. View expenses by category\n5. Exit\n\nChoose an option: ")
    match(choice):
      case 1:
        description, amount, category = "", "", ""
        individual = add_expense(description, amount, category)
        expenses.append(individual)
        print("Expense added successfully!\n")
      case 2: view_expenses(expenses)
      case 3: total_expenses(expenses)
      case 4: expenses_per_category(expenses)

  print("Goodbye!")

def get_number(prompt):
  while True:
    try:
      n = int(input(prompt))
      if n not in [1,2,3,4,5]:
        print("Choose a number between 1 and 5")
        continue
    except ValueError:
      continue
    break

  return n

def add_expense(d, a, c):
  temp = {}

  while not re.fullmatch(PATTERN_INPUT, d): d = input("\nDescription: ")
  while not re.fullmatch(PATTERN_AMOUNT, a): a = input("\nAmount: ")
  while not re.fullmatch(PATTERN_INPUT, c): c = input("\nCategory: ")

  temp["description"], temp["amount"], temp["category"] = d, a, c

  return temp

def view_expenses(ex):
  length = len(ex)
  if length != 0:
    print("=== All Expenses ===\n")
    for i in range(length):
      print(f"{i+1}.\t{ex[i]['description']}\n\tAmount: {ex[i]['amount']}\n\tCategory: {ex[i]['category']}\n")
  else:
    print("No expenses found.")

def total_expenses(ex):
  print("=== Total Expenses ===\n")
  total = 0.0
  for i in range(len(ex)):
    total += float(ex[i]["amount"])
  print(f"Total: €{total}")

def expenses_per_category(ex):
  cat = ""
  while cat == "": cat = input("\nEnter category: ").lower()

  found = False
  sum = 0.0
  desc, am = [], []
  for i in range(len(ex)):
    if cat == ex[i]["category"].lower():
      found = True
      desc.append(ex[i]["description"])
      am.append(ex[i]["amount"])

  if found:
    print(f"\n=== {cat.capitalize()} Expenses ===\n")
    for i in range(len(desc)):
      print(f"{desc[i]} - €{am[i]}")
      sum += float(am[i])
  else:
    print("\nNo expenses found in this category.")
    return

  print(f"\nCategory total: {sum}")

main()
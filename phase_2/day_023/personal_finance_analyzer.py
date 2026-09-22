import re

PATTERN_STRING = r"[A-Za-z]+"
PATTERN_INT = r"[0-9]+"

def main():
    print("=== PERSONAL FINANCE ANALYZER ===")
    choice = 0
    finance = [{"id": 1, "description": "Salary", "amount": 1100, "category": "Work", "type": "income"},{"id": 2, "description": "Supermarket", "amount": 80, "category": "Food", "type": "expense"},{"id": 3, "description": "Gym", "amount": 30, "category": "Health", "type": "expense"},{"id": 4, "description": "Freelance", "amount": 200, "category": "Work", "type": "income"},{"id": 5, "description": "Cinema", "amount": 15, "category": "Entertainment", "type": "expense"}]
    income, expenses = 0, 0
    
    while True:
        choice = get_int("Enter a number between 1 and 8: ")
        match(choice):
            case 1: show_transactions(finance)
            case 2: add_transaction(finance)
            case 3: income = total_income(finance)
            case 4: expenses = total_expenses(finance)
            case 5: show_balance(income, expenses)
            case 6: show_expenses_per_category(finance)
            case 7: search_transactions(finance)
            case _: break

    print("Goodbye!")

def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n not in [1,2,3,4,5,6,7,8]:
                continue
        except ValueError:
            continue
        break
    
    return n

def show_transactions(f):
    flag = check_emptiness(f)
    if flag:
        print("No transactions found.")
        return
    
    for i in range(len(f)):
        print(f"{f[i]['id']} | {f[i]['description']} | €{f[i]['amount']} | {f[i]['category']} | {f[i]['type']}")

def add_transaction(f):
    flag = check_emptiness(f)
    if flag:
        id = 0
    else:
        id = f[(len(f) - 1)]["id"]
    d, a, c, t = "", "", "", ""
    temp = {}
    
    while not re.fullmatch(PATTERN_STRING, d): d = input("Description: ").capitalize()
    
    while not re.fullmatch(PATTERN_INT, a): a = input("Amount: ")
    
    a = int(a)
    
    while not re.fullmatch(PATTERN_STRING, c): c = input("Category: ").capitalize()
    
    while t not in ["income", "expense"]: t = input("Type: ")
    
    temp["id"], temp["description"], temp["amount"], temp["category"], temp["type"] = id + 1, d, a, c, t
    f.append(temp)

def total_income(f):
    flag = check_emptiness(f)
    if flag:
        print("No transactions found to calculate total income.")
        return
    sum = 0
    
    for i in range(len(f)):
        if f[i]["type"] == "income":
            sum += f[i]["amount"]
    
    print(f"Total income: €{sum}")
    return sum

def total_expenses(f):
    flag = check_emptiness(f)
    if flag:
        print("No transactions found to calculate total expenses.")
        return
    sum = 0
    
    for i in range(len(f)):
        if f[i]["type"] == "expense":
            sum += f[i]["amount"]
    
    print(f"Total expenses: €{sum}")
    return sum

def show_balance(i, e):
    print(f"Total income: €{i}")
    print(f"Total expenses: €{e}")
    b = i - e
    print(f"Balance: €{b}")

def show_expenses_per_category(f):
    flag = check_emptiness(f)
    if flag:
        print("No transactions found to display expenses/category.")
        return
    print("=== EXPENSES BY CATEGORY ===")
    temp = {}
    
    for i in range(len(f)):
        if f[i]["category"] not in temp:
            temp[f[i]["category"]] = f[i]["amount"]
        else:
            temp[f[i]["category"]] += f[i]["amount"]
    
    for k, v in temp.items():
        print(f"{k}: €{v}")

def search_transactions(f):
    flag = check_emptiness(f)
    if flag:
        print("No transactions found to search.")
        return
    
    s = ""
    
    while not re.fullmatch(PATTERN_STRING, s):
        s = input("Search: ")
    
    count = 0
    
    for i in range(len(f)):
        if s.lower() in f[i]["category"].lower():
            print(f"{f[i]['id']} | {f[i]['description']} | €{f[i]['amount']} | {f[i]['category']} | {f[i]['type']}")
            count += 1
    
    if count == 0:
        print("No transaction was found.")
    

def check_emptiness(f):
    length = len(f)
    if length == 0:
        return True
    return False

main()

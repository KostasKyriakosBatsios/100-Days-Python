# Day 46 23/10/26

from datetime import datetime
import json
import re

PATTERN_STRING = r"[A-Za-z\s]+"

def main():
    print("========== EXPENSE TRACKER ==========")
    
    try:
        with open('phase_3/day_046/expenses.json', 'r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
    
    while True:
        num = get_int("\n1. Add new expense\n2. Display all expenses\n3. Search expense per category\n4. Display total expenses\n5. Display expenses per category\n6. Display most expensive expense\n7. Save and exit\n\nChoose: ")
        
        match(num):
            case 1:
                add_expense(expenses)
            case 2:
                display_all(expenses)
            case 3:
                search_expense(expenses)
            case 4:
                display_total_expenses(expenses)
            case 5:
                display_expenses_per_category(expenses)
            case 6:
                display_max_expense(expenses)
            case 7:
                save_expenses(expenses)
                break
    
    print("\nGoodbye!")


def get_int(p):
    while True:
        
        try:
            n = int(input(p))
        except ValueError:
            print("\nOnly numbers!")
            continue
        
        if 1 <= n <= 7:
            return n
        
        print("\nChoose between 1 and 7!")


def add_expense(exp):
    e_id, t, a, c, d = len(exp) + 1, "", 0.0, "", ""
    temp = {}
    
    if len(exp) != 0:
        for e in exp:
            if e_id == e['id']:
                e_id += 1
    
    while not re.fullmatch(PATTERN_STRING, t):
        t = input("\nTitle: ")
    
    while True:
        
        try:
            a = float(input("Amount: "))
        except ValueError:
            print("\nOnly numbers!")
            continue
        
        if a > 0:
            break
        
        print("\nOnly positive numbers!")
    
    while not re.fullmatch(PATTERN_STRING, c):
        c = input("Category: ")
    
    
    while True:
        d = input("Date (dd-mm-yyyy): ")
        
        if is_valid_date(d):
            break
        
        print("\nEnter a valid date!")
    
    temp["id"], temp["title"], temp["amount"], temp["category"], temp["date"] = e_id, t, a, c, d
    exp.append(temp)
    print("\nExpense added successfully!")


def is_valid_date(d, date_format="%d-%m-%Y"):
    try:
        datetime.strptime(d, date_format)
        return True
    except ValueError:
        return False


def display_all(exp):
    if not exp:
        return print("\nNo expenses found!")
    
    for e in exp:
        print(f"\nID: {e['id']}\nTitle: {e['title']}\nAmount: {e['amount']}€\nCategory: {e['category']}\nDate: {e['date']}")


def search_expense(exp):
    if not exp:
        return print("\nNo expenses found!")
    
    c, flag = "", False
    
    while not re.fullmatch(PATTERN_STRING, c):
        c = input("\nCategory: ")
    
    for e in exp:
        if c.lower() == e["category"].lower():
            print(f"\nID: {e['id']}\nTitle: {e['title']}\nAmount: {e['amount']}€\nCategory: {e['category']}\nDate: {e['date']}")
            flag = True
    
    if not flag:
        print(f"\nNo expenses with category {c} was found!")


def display_total_expenses(exp):
    if not exp:
        return print("\nNo expenses found!")
    
    total = 0.0
    
    for e in exp:
        total += e["amount"]
    
    print(f"\nTotal expenses: {total:.2f}€")


def display_expenses_per_category(exp):
    if not exp:
        return print("\nNo expenses found!")
    
    temp = {}
    
    for e in exp:
        if e["category"] not in temp:
            temp[e["category"]] = e["amount"]
        else:
            temp[e["category"]] += e["amount"]
    
    for k,v in temp.items():
        print(f"{k} : {v}€")


def display_max_expense(exp):
    if not exp:
        return print("\nNo expenses found")
    
    a_max, e_max = 0, {}
    
    for e in exp:
        if e["amount"] > a_max:
            a_max = e["amount"]
            e_max = e
    
    print(f"The most expensive expense:\nID: {e_max['id']}\nTitle: {e_max['title']}\nAmount: {e_max['amount']}\nCategory: {e_max['category']}\nDate: {e_max['date']}")


def save_expenses(exp):
    with open('phase_3/day_046/expenses.json', 'w') as f:
        json.dump(exp, f, indent=4)


main()

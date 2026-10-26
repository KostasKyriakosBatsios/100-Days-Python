# Day 47 26/10/26

from datetime import datetime
import re


PATTERN_STRING = r"[A-Za-z\s]+"


class Expense:
    def __init__(self, e_id, title, amount, category, date):
        self.e_id = e_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
    
    def exp_display(self):
        print(f"\nID: {self.e_id}\nTitle: {self.title}\nAmount: {self.amount}€\nCategory: {self.category}\nDate: {self.date}")


class ExpenseManager:
    def __init__(self):
        self.expenses = []
    
    
    def add_expense(self):
        e_id, t, a, c, d = len(self.expenses) + 1, "", 0.0, "", ""
        
        while not re.fullmatch(PATTERN_STRING, t):
            t = input("\nTitle: ")
        
        while True:
            try:
                a = float(input("\nAmount: "))
                
                if a > 0.0:
                    break
                
                print("\nOnly positive floating numbers!")
            except ValueError:
                print("\nOnly numbers!")
                continue
        
        while not re.fullmatch(PATTERN_STRING, c):
            c = input("\nCategory: ")
        
        while True:
            d = input("\nDate (dd-mm-yyyy): ")
            
            if is_valid_date(d):
                break
            
            print("\nEnter a valid date")
        
        temp = Expense(e_id, t, a, c, d)
        self.expenses.append(temp)
        print("\nExpense added successfully!")
    
    
    def display_expenses(self):
        if len(self.expenses) == 0:
            return print("\nNo expenses found.")
        
        for exp in self.expenses:
            exp.exp_display()
    
    
    def search_category_expenses(self):
        if len(self.expenses) == 0:
            return print("\nNo expenses found.")
        
        c, flag = "", False
        
        while not re.fullmatch(PATTERN_STRING, c):
            c = input("\nCategory: ")
        
        for exp in self.expenses:
            if c.lower() == exp.category.lower():
                exp.exp_display()
                flag = True
        
        if not flag:
            print(f"\nExpenses with category {c} not found!")
        
    
    def calculate_total_expenses(self):
        if len(self.expenses) == 0:
            return print("\nNo expenses found.")
        
        total = 0.0
        
        for exp in self.expenses:
            total += exp.amount
        
        print(f"\nTotal expenses: {total:.2f}€")
    
    
    def calculate_category_expenses(self):
        if len(self.expenses) == 0:
            return print("\nNo expenses found.")
        
        temp = {}
        
        for exp in self.expenses:
            if exp.category not in temp:
                temp[f"{exp.category}"] = exp.amount
            else:
                temp[f"{exp.category}"] += exp.amount
        
        for k, v in temp.items():
            print(f"{k}: {v}€")
    
    
    def most_expensive_expense(self):
        if len(self.expenses) == 0:
            return print("\nNo expenses found.")
        
        temp_max = 0.0
        
        for exp in self.expenses:
            if exp.amount >= temp_max:
                temp_max = exp.amount
                exp_max = exp
        
        print(f"Most expensive expense: ")
        exp_max.exp_display()


def main():
    print("========== EXPENSE MANAGER ==========")
    exp_obj = ExpenseManager()
    
    while True:
        number = get_int("\n1. Add expense\n2. Display expenses\n3. Search expenses/category\n4. Calculate total expenses\n5. Calculate expenses/category\n6. Most expensive expense\n7. Exit\n\nChoose: ")
        
        match(number):
            case 1:
                exp_obj.add_expense()
            case 2:
                exp_obj.display_expenses()
            case 3:
                exp_obj.search_category_expenses()
            case 4:
                exp_obj.calculate_total_expenses()
            case 5:
                exp_obj.calculate_category_expenses()
            case 6:
                exp_obj.most_expensive_expense()
            case 7:
                break
    
    print("\nGoodbye!")


def get_int(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 7:
                return n
                
            print("\nOnly integers between 1 and 7.")
        except ValueError:
            print("\nOnly numbers!")
            continue


def is_valid_date(d):
    try:
        datetime.strptime(d, "%d-%m-%Y")
        return True
    except ValueError:
        return False


main()

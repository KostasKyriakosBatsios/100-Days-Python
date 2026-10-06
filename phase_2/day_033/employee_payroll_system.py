# Day 33 6/10/26

import re

PATTERN_NAME = r"[A-Za-z\s]+"
PATTERN_LANG = r"[A-Za-z]+"

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nSalary: {self.salary}")
    
    def calculate_bonus(self):
        return (self.salary * 0.05)
    
    def calculate_total_pay(self):
        return (self.salary + self.calculate_bonus())

class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
    
    def display(self):
        super().display()
        print(f"Programming language: {self.programming_language}")
    
    def calculate_bonus(self):
        return (self.salary * 0.1)

class Manager(Employee):
    def __init__(self, id, name, salary, team_size):
        super().__init__(id, name, salary)
        self.team_size = team_size
    
    def display(self):
        super().display()
        print(f"Team size: {self.team_size}")
    
    def calculate_bonus(self):
        return (self.salary * 0.15)

class Company:
    def __init__(self):
        self.employees = []
    
    def show_employees(self):
        if len(self.employees) == 0:
            return print("\nNo employees were found!")
        
        for e in self.employees:
            e.display()
    
    def add_employee(self):
        o = 0
        
        while True:
            try:
                o = int(input("\n1. Employee\n2. Developer\n3. Manager\n\nPick: "))
                if not (1 <= o <= 3):
                    continue
                break
            except ValueError:
                continue
        
        id, nm, sl = 0, "", 0.0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
                if (len(self.employees) == 0) and not (id == 0):
                    break
                
                for e in self.employees:
                    if id == e.id:
                        print(f"\nEmployee {id} already exists!")
                        id = 0
                        break
                
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_NAME, nm):
            nm = input("Name: ")
        
        while sl == 0.0:
            try:
                sl = abs(float(input("Salary: ")))
            except ValueError:
                continue
        
        temp = None
        
        match(o):
            case 1:
                temp = Employee(id, nm, sl)
            case 2:
                lang = ""
                
                while not re.fullmatch(PATTERN_LANG, lang):
                    lang = input("Programming language: ")
                
                temp = Developer(id, nm, sl, lang)
            case 3:
                tm = 0
                
                while tm == 0:
                    try:
                        tm = abs(int(input("Team size: ")))
                    except ValueError:
                        continue
                
                temp = Manager(id, nm, sl, tm)
        
        self.employees.append(temp)
    
    def find_employee(self):
        if len(self.employees) == 0:
            return print("\nNo employees were found!")
        
        id = 0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        flag = False
        
        for e in self.employees:
            if id == e.id:
                e.display()
                flag = True
        
        if not flag:
            print(f"\nEmployee {id} isn't on the company.")
    
    def show_bonuses(self):
        if len(self.employees) == 0:
            return print("\nNo employees were found!")
        
        for e in self.employees:
            print(f"\nName: {e.name}\nSalary: {e.salary}\nBonus: {e.calculate_bonus()}\nTotal pay: {e.calculate_total_pay()}")
    
    def statistics(self):
        if len(self.employees) == 0:
            return print("\nNo employees were found!")
        
        total_e, total_sl, total_b, total_pay, max_paid, max_b = 0, 0, 0, 0, 0, 0
        name_max_paid, id_max_paid = "", 0
        name_max_b, id_max_b = "", 0
        
        for e in self.employees:
            bonus = e.calculate_bonus()
            salary = e.salary
            total_e += 1
            total_sl += salary
            total_b += bonus
            total_pay += e.calculate_total_pay()
            if salary > max_paid:
                max_paid = salary
                name_max_paid = e.name
                id_max_paid = e.id
            if bonus > max_b:
                max_b = bonus
                name_max_b = e.name
                id_max_b = e.id
        
        print(f"\nTotal employees: {total_e}\nTotal salaries: {total_sl}\nTotal bonuses: {total_b}\nTotal payroll: {total_pay}\nAverage salary: {(total_sl/total_e):.2f}")
        print(f"\nHighest paid employee:\nName: {name_max_paid}\nID: {id_max_paid}\nSalary: {max_paid}")
        print(f"\nHighest bonus:\nName: {name_max_b}\nID: {id_max_b}\nBonus: {max_b}")

def main():
    print("===== EMPLOYEE PAYROLL SYSTEM =====")
    company = Company()
    
    while True:
        num = get_int("\n1. Show employees\n2. Add employee\n3. Find employee\n4. Show bonuses\n5. Show statistics\n6. Exit\n\nChoose: ")
        match(num):
            case 1: company.show_employees()
            case 2: company.add_employee()
            case 3: company.find_employee()
            case 4: company.show_bonuses()
            case 5: company.statistics()
            case 6: break
    
    print("\nGoodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            return n if (1 <= n <= 6) else print("\nChoose between 1 and 6!")
        except ValueError:
            continue

main()

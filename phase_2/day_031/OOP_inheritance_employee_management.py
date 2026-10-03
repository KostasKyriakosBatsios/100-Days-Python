# Day 031 3/10/26

import re

PATTERN_NAME = r"^[A-Za-z\s]+$"

# Parent class
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nSalary: {self.salary}")

    def calculate_bonus(self):
        return self.salary + (self.salary * 0.05)

# Child class
class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        super().__init__(id, name, salary)
        self.programming_language = programming_language

    # Polymorphism: Overriding the display method
    def display(self):
        super().display()
        print(f"Type: Developer\nProgramming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary + (self.salary * 0.10)

# Child class
class Manager(Employee):
    def __init__(self, id, name, salary, team_size):
        super().__init__(id, name, salary)
        self.team_size = team_size
    
    # Polymorphism: Overriding the display method
    def display(self):
        super().display()
        print(f"Type: Manager\nTeam Size: {self.team_size}")

    def calculate_bonus(self):
        return self.salary + (self.salary * 0.15)

class Company:
    def __init__(self):
        self.employees = []

    def show_employees(self):
        if len(self.employees) == 0:
            return print("\nNo employees found.")

        for employee in self.employees:
            employee.display()

    def add_employee(self, type):
        id, nm, sal = 0, "", 0.0

        while True:
            try:
                id = int(input("\nID: "))
                if len(self.employees) == 0:
                    break
                flag = False
                
                for employee in self.employees:
                    if employee.id == id:
                        print(f"\nEmployee {id} already exists.")
                        flag = True
                        break

                if not flag:
                    break
            except ValueError:
                continue

        while not re.fullmatch(PATTERN_NAME, nm):
            nm = input("Name: ")

        while sal <= 0.0:
            try:
                sal = float(input("Salary: "))
            except ValueError:
                continue

        match(type):
            case 2: temp = Employee(id, nm, sal)
            case 3:
                pl = ""
                while pl == "":
                    pl = input("Programming Language: ")
                temp = Developer(id, nm, sal, pl)
            case 4:
                ts = 0
                while ts <= 0:
                    try:
                        ts = int(input("Team Size: "))
                    except ValueError:
                        continue
                temp = Manager(id, nm, sal, ts)
        self.employees.append(temp)

    def find_employee(self):
        if len(self.employees) == 0:
            return print("\nNo employees found.")

        id = 0
        while id <= 0:
            try:
                id = int(input("\nID: "))
            except ValueError:
                continue

        for employee in self.employees:
            if employee.id == id:
                return employee.display()

    def show_bonuses(self):
        if len(self.employees) == 0:
            return print("\nNo employees found.")

        for employee in self.employees:
            employee.display()
            print(f"Bonus: {employee.calculate_bonus()}\n")

    def statistics(self):
        if len(self.employees) == 0:
            return print("\nNo employees found.")

        total_emp, count_dev, count_man, total_sal, total_bonus = 0, 0, 0, 0.0, 0.0

        for employee in self.employees:
            total_emp += 1
            total_sal += employee.salary
            total_bonus += employee.calculate_bonus()
            if isinstance(employee, Developer):
                count_dev += 1
            elif isinstance(employee, Manager):
                count_man += 1

        print(f"\nTotal Employees: {total_emp}\nDevelopers: {count_dev}\nManagers: {count_man}\nAverage Salary: {(total_sal / total_emp):.2f}\nTotal Salaries: {total_sal}\nTotal Bonuses: {total_bonus}")

def main():
    print("========== COMPANY ==========")
    company = Company()

    while True:
        num = get_int("\n1. Show employees\n2. Add employee\n3. Add developer\n4. Add manager\n5. Find employee\n6. Show bonuses\n7. Show statistics\n8. Exit\n\nChoose: ")
        match(num):
            case 1: company.show_employees()
            case 2: company.add_employee(2)
            case 3: company.add_employee(3)
            case 4: company.add_employee(4)
            case 5: company.find_employee()
            case 6: company.show_bonuses()
            case 7: company.statistics()
            case 8: break

    print("\nGoodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            return n if (1 <= n <= 8) else print("\nChoose between 1 and 8")
        except ValueError:
            continue
        
main()

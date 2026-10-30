# Day 53 30/10/26

class Employee:
    def __init__(self, employee_id, name, position, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department
    
    
    def display_info(self):
        print(f"\nEmployee ID: {self.employee_id}\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}\nDepartment: {self.department}")
    
    
    def increase_salary(self, percentage):
        self.salary += self.salary * percentage


class EmployeeManager:
    def __init__(self):
        self.employees = []
    
    
    def add_employee(self):
        e_id, n, p, s, d = 1, "", "", 0.0, ""
        existing_ids = {e.employee_id for e in self.employees}
        
        while e_id in existing_ids:
            e_id += 1
                    
        while not n:
            n = input("\nName: ").strip()
            
            if any(c.isdigit() for c in n):
                print("\nNo numbers in name!")
                n = ""
        
        while not p:
            p = input("\nPosition: ").strip()
            
            if any(c.isdigit() for c in p):
                print("\nNo numbers in position!")
                p = ""
        
        while True:
            try:
                s = float(input("\nSalary: "))
            except ValueError:
                print("\nOnly Numbers!")
                continue
            
            if s > 0.0:
                break
                
            print("\nOnly positive floating numbers!")
        
        while not d:
            d = input("\nDepartment: ").strip()
            
            if any(c.isdigit() for c in d):
                print("\nNo numbers in department!")
                d = ""
        
        self.employees.append(Employee(e_id, n, p, s, d))
        print("\nEmployee was added successfully!")
    
    
    def display_employees(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        for e in self.employees:
            e.display_info()
    
    
    def search_employee(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        txt, flag = "", False
        
        while not txt:
            txt = input("\nEnter either the ID or the name of the employee: ").strip()
            
            if txt.isdigit():
                txt = int(txt)
                break
        
        for e in self.employees:
            if isinstance(txt, int):
                if txt == e.employee_id:
                    flag = True
                    e.display_info()
            else:
                if txt.lower() == e.name.lower():
                    flag = True
                    e.display_info()
        
        if not flag:
            print(f"\nNo employee with name/ID {txt} was found!")
    
    
    def remove_employee(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        e_id, flag = 0, False
        
        while True:
            try:
                e_id = int(input("\nEmployee ID: "))
            except ValueError:
                print("\nOnly numbers!")
                continue
            
            if e_id > 0:
                break
            
            print("\nOnly positive integers!")
        
        for e in self.employees:
            if e_id == e.employee_id:
                flag = True
                ch = ''
        
                while ch not in ['y', 'n']:
                    ch = input("\nAre you sure? [y/n]").lower()
        
                if ch == 'n':
                    return print("\nOK. The employee will not be removed!")
        
                self.employees.remove(e)
                return print(f"\nThe employee with ID {e_id} was removed!")
        
        if not flag:
            return print(f"\nEmployee with ID {e_id} wasn't found!")
        
        
    
    
    def increase_employee_salary(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        e_id, flag, pr, pos = 0, False, 0.0, 0
        
        while True:
            try:
                e_id = int(input("\nEmployee ID: "))
            except ValueError:
                print("\nOnly numbers")
                continue
            
            if e_id > 0:
                break
            
            print("\nOnly positive integers!")
        
        for i, e in enumerate(self.employees):
            if e_id == e.employee_id:
                flag = True
                pos = i
        
        if not flag:
            return print(f"\nNo employee with ID {e_id} was found!")
        
        while True:
            try:
                pr = float(input("\nHow much (%)? "))
            except ValueError:
                print("\nOnly numbers!")
                continue
            
            if pr > 0.0:
                break
                
            print("\nOnly positive percentages!")
        
        self.employees[pos].increase_salary(pr/100)
        print(f"\nThe increase in the salary of employee with ID {e_id} was successful!")
    
    
    def display_department(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        d, emp = "", []
        
        while not d:
            d = input("\nDepartment: ").strip()
            
            if any(c.isdigit() for c in d):
                print("\nNo numbers in department!")
                d = ""
        
        for e in self.employees:
            if d.lower() == e.department.lower():
                emp.append(e)
        
        if not emp:
            return print(f"\nDepartment {d} not found!")
        
        for e in emp:
            e.display_info()
    
    
    def display_highest_paid(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        s_max = max(e.salary for e in self.employees)
        
        for e in self.employees:
            if e.salary == s_max:
                e.display_info()
        
    
    def display_statistics(self):
        if not self.employees:
            return print("\nNo employees were found!")
        
        count_e, total_s = len(self.employees), 0.0
        max_s = max(e.salary for e in self.employees)
        min_s = min(e.salary for e in self.employees)
        temp = {}
        
        for e in self.employees:
            total_s += e.salary
            
            if e.department not in temp:
                temp[f"{e.department}"] = 1
            else:
                temp[f"{e.department}"] += 1
        
        print(f"\nTotal employees: {count_e}\nAverage salary: {(total_s/count_e):.2f}\nHighest salary: {max_s}\nLowest salary: {min_s}\nTotal employees per department:")
        
        for k, v in temp.items():
            print(f"{k}: {v}")


def main():
    print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
    
    manager = EmployeeManager()
    
    while True:
        num = get_num("\n1. Add Employee\n2. Display All Employees\n3. Search Employee\n4. Remove Employee\n5. Increase Salary\n6. Display Department\n7. Highest Paid Employee\n8. Display statistics\n9. Exit\n\nChoose: ")
        
        match num:
            case 1:
                manager.add_employee()
            case 2:
                manager.display_employees()
            case 3:
                manager.search_employee()
            case 4:
                manager.remove_employee()
            case 5:
                manager.increase_employee_salary()
            case 6:
                manager.display_department()
            case 7:
                manager.display_highest_paid()
            case 8:
                manager.display_statistics()
            case 9:
                break
    
    print("\nGoodbye!")


def get_num(p):
    while True:
        try:
            n = int(input(p))
        except ValueError:
            print("\nOnly numbers!")
            continue
        
        if 1 <= n <= 9:
            return n
                
        print("\nOnly integers between 1 and 9!")

main()

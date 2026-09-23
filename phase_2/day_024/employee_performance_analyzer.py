import re

PATTERN_NAME = r"[A-Za-z\s]+"
PATTERN_DEP = r"[A-Z]{1,2}"

def main():
    print("====== EMPLOYEE PERFORMANCE ANALYZER ======\n")
    choice = 0
    employees = []
    while True:
        choice = get_number("Choose between 1 and 8: ")
        match(choice):
            case 1: show_employees(employees)
            case 2: add_employee(employees)
            case 3: show_average(employees)
            case 4: show_dept_average(employees)
            case 5: show_highest_performer(employees)
            case 6: search_employee(employees)
            case 7: show_statistics(employees)
            case _: break
    
    print("Goodbye!")

def get_number(pr):
    while True:
        try:
            n = int(input(pr))
            if not (1 <= n <= 8):
                continue
            break
        except ValueError:
            continue
    
    return n
    
def show_employees(e):
    if check_emptiness(e):
        print("\nNo employees were found.\n")
        return

    print()

    for i in range(len(e)):
        print(f"{e[i]['id']} | {e[i]['name']} | {e[i]['department']}\nScores: {', '.join(str(score) for score in e[i]['scores'])}")

    print()

def add_employee(e):
    if check_emptiness(e):
        id = 0
    else:
        id = len(e)
    
    temp = {}
    n, d, sc, sc_list = "", "", 0, []
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nName: ")
        if not check_emptiness(e):
            for i in range(len(e)):
                if n.lower() == e[i]["name"].lower():
                    print("\nEmployee already exists!\n")
                    n = ""
                    break
    
    while not re.fullmatch(PATTERN_DEP, d):
        d = input("Department: ")
    
    num = 0
    
    while True:
        try:
            num = int(input("How many scores? "))
            if num <= 0:
                print("\nNumber must be positive!")
                continue
            break
        except ValueError:
            continue
    
    i = 1
    
    while i <= num:
        try:
            sc = int(input(f"Score {i}: "))
            if not (0 <= sc <= 100):
                print("\nNumber must be between 0 and 100")
                continue
            sc_list.append(sc)
            i += 1
        except ValueError:
            continue
    
    temp["id"], temp["name"], temp["department"], temp["scores"] = id + 1, n, d, sc_list
    e.append(temp)
    print("\nEmployee added successfully!\n")

def show_average(e):
    if check_emptiness(e):
        print("\nNo employees were found.\n")
        return
    
    n = ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nEnter employee name: ")
    
    flag, total, pop = False, 0, 0
    
    for i in range(len(e)):
        if n.lower() == e[i]["name"].lower():
            for j in range(len(e[i]["scores"])):
                flag = True
                total += e[i]["scores"][j]
                pop += 1

    if flag:
        avg = total / pop
        print(f"\n{n}'s average: {avg:.2f}")
        return
    
    print(f"\nNo employee with the name {n} was found.\n")

def show_dept_average(e):
    if check_emptiness(e):
        print("\nNo employees were found.\n")
        return
    temp, avg = {}, 0
    
    for i in range(len(e)):
        total, pop = 0, 0
        
        for j in range(len(e[i]["scores"])):
            total += e[i]["scores"][j]
            pop += 1
            
        avg = total / pop
        if e[i]["department"] not in temp:
            temp[f"{e[i]["department"]}"] = avg
        else:
            temp[f"{e[i]["department"]}"] += avg
    
    print("\n===== DEPARTMENT AVERAGES =====")
    
    for k, v in temp.items():
        print(f"\n{k}: {v:.2f}")

    print()
    
def show_highest_performer(e):
    if check_emptiness(e):
        print("\nNo employees were found.\n")
        return
    length = len(e)
    avg = 0
    
    for i in range(length):
        total, pop = 0, 0
        
        for j in range(len(e[i]["scores"])):
            total += e[i]["scores"][j]
            pop += 1
            
        avg = total / pop
        e[i]["average"] = avg

    name, dept, max = "", "", 0
    print("\n===== TOP PERFORMER =====")
    
    for i in range(length):
        if e[i]["average"] > max:
            max = e[i]["average"]
            dept = e[i]["department"]
            name = e[i]["name"]
    
    print(f"\nEmployee: {name}\nDepartment: {dept}\nAverage: {max:.2f}\n")

def search_employee(e):
    if check_emptiness(e):
        print("\nNo employees were found.\n")
        return
    
    n = ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nSearch: ")

    print()
    
    for i in range(len(e)):
        if n.lower() in e[i]["name"].lower():
            print(f"{e[i]['name']} | {e[i]['department']} | Average: {e[i]['average']}")

    print()

def show_statistics(e):
    if check_emptiness(e):
        print("\nNo employees were found.\n")
        return
    
    print("\n===== STATISTICS =====")
    length = len(e)
    count_emp, count_dep, max, min, total_avg, count_ab_80, count_bl_50 = 0, 0, 0, 1000, 0, 0, 0
    temp = []
    
    for i in range(length):
        total, pop = 0, 0
        
        for j in range(len(e[i]["scores"])):
            total += e[i]["scores"][j]
            pop += 1
            
        avg = total / pop
        e[i]["average"] = avg
    
    for i in range(length):
        count_emp += 1
        if e[i]["department"] not in temp:
            temp.append(e[i]["department"])
            count_dep += 1

        if e[i]["average"] > max:
            max = e[i]["average"]

        if e[i]["average"] < min:
            min = e[i]["average"]

        if e[i]["average"] > 80:
            count_ab_80 += 1
        elif e[i]["average"] < 50:
            count_bl_50 += 1
        total_avg += e[i]["average"]
    
    total_avg /= count_emp
    print(f"\nTotal employees: {count_emp}\nDepartments: {count_dep}\n\nHighest average: {max}\nLowest average: {min}\nOverall average: {total_avg}\n\nEmployees above 80: {count_ab_80}\nEmployees below 50: {count_bl_50}\n")

def check_emptiness(e):
    length = len(e)
    if length == 0:
        return True
    return False

main()

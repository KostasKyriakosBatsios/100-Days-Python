# Day 28 30/9/26

import re

PATTERN_TITLE = r"[A-Za-z\s]+"
PATTERN_NUMBERS = r"[0-9]+"

class Task:
    def __init__(self, id, title, priority):
        self.id = id
        self.title = title
        self.priority = priority
        self.completed = False
    
    def complete(self):
        self.completed = True
    
    def print_info(self):
        status = "Completed" if self.completed else "Pending"
        print(f"#{self.id} | {self.title} | {self.priority} | {status}")

class TaskManager:
    def __init__(self):
        self.tasks = []

def main():
    print("====== TASK MANAGER ======")
    manager = TaskManager()
    tasks = manager.tasks
    
    while True:
        num = get_int("\n1. Show tasks\n2. Add task\n3. Complete task\n4. Delete task\n5. Search task\n6. Filter by priority\n7. Show statistics\n8. Exit\n\nChoose: ")
        match(num):
            case 1: show_tasks(tasks)
            case 2: add_task(tasks)
            case 3: complete_task(tasks)
            case 4: delete_task(tasks)
            case 5: search_task(tasks)
            case 6: filter_priority(tasks)
            case 7: statistics(tasks)
            case 8: break
    
    print("Goodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            if not (1 <= n <= 8):
                continue
            break
        except ValueError:
            continue
    
    return n

def show_tasks(t):
    if check_emptiness(t):
        print("No tasks were found!")
        return 0
    
    for i in range(len(t)):
        t[i].print_info()

def add_task(t):
    id = 0 if check_emptiness(t) else len(t)
    txt, pr = "", ""
    
    while not re.fullmatch(PATTERN_TITLE, txt): txt = input("Title: ")
    
    while pr not in ["Low", "Medium", "High"]: pr = input("Priority: ")
    
    temp = Task(id + 1, txt, pr)
    t.append(temp)

def complete_task(t):
    if check_emptiness(t):
        print("No tasks were found!")
        return 0
    
    n = ""
    
    while not re.fullmatch(PATTERN_NUMBERS, n): n = input("Enter task ID: ")
    
    n = int(n)
    flag = False
    
    for i in range(len(t)):
        if n == t[i].id:
            if t[i].completed:
                print("The task is already completed.")
                return 0
            t[i].complete()
            flag = True
    
    if flag:
        print(f"Task {n} completed!")
        return 0
    
    print(f"No task {n} was found to complete")

def delete_task(t):
    if check_emptiness(t):
        print("No tasks were found!")
        return 0
    
    n = ""
    
    while not re.fullmatch(PATTERN_NUMBERS, n): n = input("Enter task ID: ")
    
    n = int(n)
    flag = False
    
    for i in range(len(t)):
        if n == t[i].id:
            t.pop(i)
            flag = True
            break

    if flag:
        print(f"Task {n} removed!")

        for i in range(len(t)):
            t[i].id = i + 1

        return 0
    
    print(f"No task {n} was found to be removed!")

def search_task(t):
    if check_emptiness(t):
        print("No tasks were found!")
        return 0
    
    txt = ""
    
    while not re.fullmatch(PATTERN_TITLE, txt): txt = input("Search: ")
    
    for i in range(len(t)):
        if txt.lower() in t[i].title.lower():
            t[i].print_info()

def filter_priority(t):
    if check_emptiness(t):
        print("No tasks were found!")
        return 0
    
    pr = ""
    
    while pr not in ["Low", "Medium", "High"]: pr = input("Choose between the 3 priorities: ")
    
    for i in range(len(t)):
        if pr == t[i].priority:
            t[i].print_info()

def statistics(t):
    if check_emptiness(t):
        print("No tasks were found!")
        return 0
    
    print("====== STATISTICS ======")
    
    total, count_com, count_pen, count_h, count_m, count_l = 0, 0, 0, 0, 0, 0
    
    for i in range(len(t)):
        total += 1
        if t[i].completed:
            count_com += 1
        else:
            count_pen += 1
        if t[i].priority == "High":
            count_h += 1
        elif t[i].priority == "Medium":
            count_m += 1
        else:
            count_l += 1
    
    rate = count_com / total
    print(f"Total tasks: {total}\nCompleted: {count_com}\nPending: {count_pen}\n\nHigh priority: {count_h}\nMedium priority: {count_m}\nLow priority: {count_l}\n\nCompletion rate: {(rate*100):.2f}%")

def check_emptiness(t):
    if len(t) == 0:
        return True
    return False

main()

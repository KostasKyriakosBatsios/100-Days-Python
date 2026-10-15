# Day 40 15/10/26

import json
import re

PATTERN_STRING = r"[A-Za-zΑ-Ζα-ζςΆΈΉΊΎΪΫάέήίύϊϋ0-9\s]+"

def main():
    print("====== CLI TASK MANAGER ======")
    
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    
    while True:
        num = get_int("\n1. Add Task\n2. Display all tasks\n3. Complete task\n4. Display pending tasks\n5. Task statistics\n6. Exit\n\nChoose: ")
        match(num):
            case 1: add_task(tasks)
            case 2: display_all_tasks(tasks)
            case 3: complete_task(tasks)
            case 4: display_pending_tasks(tasks)
            case 5: display_stats(tasks)
            case 6: 
                save_tasks(tasks)
                break

def get_int(p):
    while True:
        try:
            n = int(input(p))
            if 1 <= n <= 6:
                return n
            print("\nChoose between 1 and 6!")
        except ValueError:
            print("\nChoose a number!")
            continue

def add_task(t):
    t_id = len(t) + 1
                
    title, desc, dummy = "", "", {}
    
    while not re.fullmatch(PATTERN_STRING, title):
        title = input("\nTitle: ")
    
    while not re.fullmatch(PATTERN_STRING, desc):
        desc = input("Description: ")
    
    dummy["id"], dummy["title"], dummy["description"], dummy["completed"] = t_id, title, desc, False
    t.append(dummy)
    print("\nTask added successfully!")

def display_all_tasks(t):
    if len(t) == 0:
        return print("\nNo tasks found!")
    
    print("\n====== ALL TASKS ======\n")
    
    for temp in t:
        print(f"#{temp['id']} | {temp['title']} | {temp['description']} | {temp['completed']}")

def complete_task(t):
    if len(t) == 0:
        return print("\nNo tasks found!")
    
    t_id, flag = 0, False
    while True:
        try:
            t_id = int(input("\nTask ID: "))
            if t_id > 0:
                break
            print("\nNumber cannot be non positive!")
        except ValueError:
            print("\nMust be a number!")
            continue
    
    for temp in t:
        if t_id == temp["id"]:
            flag = True
            if not temp["completed"]:
                temp["completed"] = True
                return print("\nTask completed successfully!")
            else:
                return print("\nTask already completed!")
    
    if not flag:
        print(f"\nTask ID {t_id} not found!")
                

def display_pending_tasks(t):
    if len(t) == 0:
        return print("\nNo tasks found!")
    
    print("\n====== PENDING TASKS ======\n")
    
    for temp in t:
        if not temp["completed"]:
            print(f"#{temp['id']} | {temp['title']} | {temp['description']} | {temp['completed']}")

def display_stats(t):
    if len(t) == 0:
        return print("\nNo tasks found!")
    total_t, total_c, total_nc = len(t), 0, 0
    
    for temp in t:
        if temp["completed"]:
            total_c += 1
        else:
            total_nc += 1
    
    print(f"\nTotal tasks: {total_t}\nCompleted: {total_c}\nNot completed: {total_nc}")

def save_tasks(t):
    with open("tasks.json", "w") as f:
        json.dump(t, f, indent=4)

main()

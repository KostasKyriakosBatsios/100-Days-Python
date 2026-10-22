# Day 45 22/10/26

import re
import sqlite3

PATTERN_STRING = r"[A-Za-z0-9:.,!\s]+"

conn = sqlite3.connect('../day_044/tasks.db')
cursor = conn.cursor()

def main():
    print("========== TASK DATABASE ANALYZER ==========")
    
    while True:
        num = get_int("\n1. Display all tasks\n2. Display completed tasks\n3. Display non completed tasks\n4. Search title of task\n5. Sort tasks based on title\n6. Display stats\n7. Exit\n\nChoose: ")
        
        match(num):
            case 1:
                display_tasks(cursor)
            case 2:
                display_completed(cursor)
            case 3:
                display_non_completed(cursor)
            case 4:
                search_task(cursor)
            case 5:
                sort_tasks(cursor)
            case 6:
                show_stats(cursor)
            case 7:
                break
    
    print("\nGoodbye!")


def get_int(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 7:
                return n
            
            print("\nChoose integers between 1 and 7!")
        except ValueError as e:
            print(e)
            continue


def display_tasks(c):
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo data found!")
    
    for row in data:
        print(row)


def display_completed(c):
    c.execute("SELECT * FROM tasks WHERE completed = 1")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo completed data found!")
    
    for row in data:
        print(row)


def display_non_completed(c):
    c.execute("SELECT * FROM tasks WHERE completed = 0")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo non completed data found!")
    
    for row in data:
        print(row)


def search_task(c):
    t = ""
    
    while not re.fullmatch(PATTERN_STRING, t):
        t = input("\nTitle of task: ")
    
    c.execute("SELECT * FROM tasks WHERE title LIKE ?", [f"%{t}%"])
    data = c.fetchall()
    
    if len(data) == 0:
        return print(f"\nNo task with title <<{t}>> found!")
    
    for row in data:
        print(row)


def sort_tasks(c):
    c.execute("SELECT * FROM tasks ORDER BY title")
    data = c.fetchall()
    
    if not data:
        return print("\nNo data found!")
    
    for row in data:
        print(row)


def show_stats(c):
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo data found!")
    
    c.execute("SELECT COUNT(*) FROM tasks")
    tasks = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")
    completed = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM tasks WHERE completed = 0")
    non_completed = c.fetchone()[0]
    print(f"\nTotal tasks: {tasks}\nCompleted: {completed}\nNon completed: {non_completed}\nCompletion rate: {((completed/tasks)*100):.2f}%")

try:
    main()
finally:
    conn.close()

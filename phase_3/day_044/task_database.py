# Day 44 21/10/26

import re
import sqlite3

# Connect
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

PATTERN_STRING = r"[A-Za-z\s]+"

def main():
    print("========== TASK DATABASE ==========")
    
    # Create db
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0
        )
    ''')
    
    while True:
        num = get_int("\n1. Add task\n2. Display all tasks\n3. Search task by ID\n4. Mark task as completed\n5. Delete task\n6. Exit\n\nChoose: ")
        
        match(num):
            case 1:
                add_task(cursor)
            case 2:
                display_tasks(cursor)
            case 3:
                search_id(cursor)
            case 4:
                complete_task(cursor)
            case 5:
                delete_task(cursor)
            case 6:
                break
        
    conn.close()
    print("\nGoodbye!")


def get_int(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 6:
                return n
            
            print("\nChoose between 1 and 6!")
        except ValueError:
            print("\nOnly integer numbers!")


def add_task(c):
    t, dsc = "", ""
    
    while not re.fullmatch(PATTERN_STRING, t):
        t = input("\nTitle: ")
    
    while not re.fullmatch(PATTERN_STRING, dsc):
        dsc = input("\nDescription: ")
    
    # Insert
    c.execute("INSERT INTO tasks ('title', 'description') VALUES (?, ?)", (t, dsc))
    conn.commit()
    print("\nTask added successfully!")


def display_tasks(c):
    
    # Select 
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo data found!")
    
    for r in data:
        print(r)


def search_id(c):
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo data found!")
    
    t_id = 0
    
    while True:
        try:
            t_id = int(input("\nTask ID: "))
            
            if t_id > 0:
                break
            
            print("\nThe ID must be a positive number!")
        except ValueError:
            print("\nOnly integer numbers!")
    
    c.execute("SELECT * FROM tasks WHERE id = ?", (t_id,))
    t = c.fetchone()
    
    if t is None:
        return print(f"\nTask with ID {t_id} not found!")
    
    print(t)


def complete_task(c):
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo data found!")
    
    t_id = 0
    
    while True:
        try:
            t_id = int(input("\nTask ID: "))
            
            if t_id > 0:
                break
            
            print("\nThe ID must be a positive number!")
        except ValueError:
            print("\nOnly integer numbers!")
    
    c.execute("SELECT * FROM tasks WHERE id = ?", [t_id])
    t = c.fetchone()
    
    if t is None:
        return print(f"\nTask with ID {t_id} not found!")
    
    if t[3] == 1:
        return print(f"\nTask with ID {t_id} already completed!")
    
    # Update
    c.execute("UPDATE tasks SET completed = ? WHERE id = ?", (1, t_id))
    conn.commit()
    print(f"\nTask with ID {t_id} completed successfully!")


def delete_task(c):
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    
    if len(data) == 0:
        return print("\nNo data found!")
    
    t_id = 0
    
    while True:
        try:
            t_id = int(input("\nTask ID: "))
            
            if t_id > 0:
                break
            
            print("\nThe ID must be a positive number!")
        except ValueError:
            print("\nOnly integer numbers!")
    
    c.execute("SELECT * FROM tasks WHERE id = ?", [t_id])
    t = c.fetchone()
    
    if t is None:
        return print(f"\nTask with ID {t_id} not found!")
    
    ch = ""
    
    while ch not in ['y', 'n']:
        ch = input(f"\nAre you sure you wanna delete task with ID {t_id}? (y/n)\n-").lower()
    
    if ch == 'n':
        return print(f"\nOK. Task with ID {t_id} will not be deleted!")
    
    # Delete
    c.execute("DELETE FROM tasks WHERE id = ?", [t_id])
    conn.commit()
    print(f"\nTask with ID {t_id} deleted successfully")


main()

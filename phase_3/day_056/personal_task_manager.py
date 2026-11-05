# Day 56 5/11/26

from datetime import datetime
import json

class Task:
    def __init__(self, task_id, description, category, date, completed):
        self.task_id = task_id
        self.description = description
        self.category = category
        self.date = date
        self.completed = completed


class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else []
        
        
        if self.tasks:
            temp = []
            for t in self.tasks:
                t['date'] = datetime.strptime(t['date'], "%d-%m-%Y")
                obj = Task(t['task_id'], t['description'], t['category'], t['date'], t['completed'])
                temp.append(obj)
        
            self.tasks = temp
    
    
    def add_task(self):
        t_id, des, cat, dt, com = 1, "", "", "", None
        ids = [t.task_id for t in self.tasks]
        
        while t_id in ids:
            t_id += 1
        
        while not des.strip():
            des = input("\nDescription: ")
            
            if des.isdigit():
                print("\nNot only numbers!")
            
        while not cat.strip():
            cat = input("\nCategory: ")
            
            if cat.isdigit():
                print("\nNot only numbers!")
        
        while not dt.strip():
            dt = input("\nDate (dd-mm-yyyy): ")
            
            try:
                dt = datetime.strptime(dt, "%d-%m-%Y")
                break
            except ValueError:
                print("\nOnly format dd-mm-yyyy is acceptable")
                dt = ""
        
        while com is None:
            com = input("\nCompleted: ").capitalize()
            
            if com == "True":
                com = True
                break
            elif com == "False":
                com = False
                break
            else:
                print("\nEither True or False are acceptable answers!")
                com = None
        
        self.tasks.append(Task(t_id, des, cat, dt, com))
        print("\nTask was created!")
        self.save_to_file()
    
    
    def show_tasks(self):
        if not self.tasks:
            return print("\nNo tasks were found!")
        
        for t in self.tasks:
            print(f"\nTask ID: {t.task_id}\nDescription: {t.description}\nCategory: {t.category}\nDate: {t.date.strftime('%d-%m-%Y')}\nCompleted: {t.completed}")
    
    
    def complete_task(self):
        if not self.tasks:
            return print("\nNo tasks were found!")
        
        t_id = 0
        
        while True:
            t_id = input("\nTask ID: ")
            
            if t_id.isdigit() and int(t_id) > 0:
                t_id = int(t_id)
                break
            
            print("\nOnly positive integers!")
        
        for t in self.tasks:
            if t_id == t.task_id:
                if t.completed:
                    return print("\nTask already completed!")
                t.completed = True
                return print(f"\nThe task with ID {t_id} was completed!")
        
        print(f"\nNo task with ID {t_id} was found!")
        self.save_to_file()
    
    
    def delete_task(self):
        if not self.tasks:
            return print("\nNo tasks were found!")
        
        t_id = 0
        
        while True:
            t_id = input("\nTask ID: ")
            
            if t_id.isdigit() and int(t_id) > 0:
                t_id = int(t_id)
                break
            
            print("\nOnly positive integers!")
        
        for t in self.tasks:
            if t_id == t.task_id:
                self.tasks.remove(t)
                return print(f"\nThe task with ID {t_id} was removed!")
        
        print(f"\nNo task with ID {t_id} was found!")
        self.save_to_file()
    
    
    def display_non_completed(self):
        if not self.tasks:
            return print("\nNo tasks were found!")
        
        flag = False
        
        for t in self.tasks:
            if not t.completed:
                flag = True
                print(f"\nTask ID: {t.task_id}\nDescription: {t.description}\nCategory: {t.category}\nDate: {t.date.strftime('%d-%m-%Y')}\nCompleted: {t.completed}")
        
        if not flag:
            print("\nAll tasks are completed!")
        
    
    def save_to_file(self):
        dt, temp = [], {}
        
        for t in self.tasks:
            temp = vars(t).copy()
            temp['date'] = t.date.strftime("%d-%m-%Y")
            dt.append(temp)
        
        with open('phase_3/day_056/tasks.json', 'w') as f:
            json.dump(dt, f, indent=4)


def main():
    print("===== PERSONAL TASK MANAGER =====")
    
    try:
        with open('phase_3/day_056/tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    
    obj = TaskManager(tasks)
    
    while True:
        num = get_int("\n1. Add Task\n2. Show Tasks\n3. Complete Task\n4. Delete Task\n5. Display Unfinished\n6. Exit\n\nChoose an option: ")
        
        match num:
            case 1:
                obj.add_task()
            case 2:
                obj.show_tasks()
            case 3:
                obj.complete_task()
            case 4:
                obj.delete_task()
            case 5:
                obj.display_non_completed()
            case 6:
                break
    
    print("\nGoodbye!")


def get_int(p):
    while True:
        n = input(p)
        
        if n.isdigit() and 1 <= int(n) <= 6:
            return int(n)
        
        print("\nOnly integers between 1 and 6!")


main()

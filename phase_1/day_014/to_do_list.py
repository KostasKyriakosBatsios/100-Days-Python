import re

PATTERN_TASK = r"[A-Za-z\s]+"

def main():
  print("=== To-Do List ===")
  choice = 0
  tasks = []
  
  while choice != 5:
    choice = get_int("\n1. View Tasks\n2. Add task\n3. Complete task\n4. Delete task\n5. Exit\n\nChoose an option: ")
    match(choice):
      case 1: view_tasks(tasks)
      case 2: add_task(tasks)
      case 3: complete_task(tasks)
      case 4: delete_task(tasks)

  print("Goodbye!")

def get_int(prompt):
  while True:
    try:
      n = int(input(prompt))
      if n not in [1,2,3,4,5]:
        print("Choose a number between 1 and 5")
        continue
    except ValueError:
      continue
    break

  return n

def view_tasks(t):
  length = len(t)
  if length != 0:
    print("\n=== Your Tasks ===\n")
    
    for i in range(length):
      print(f"{i+1}. {t[i]['task']}")
      
  else:
    print("\nNo tasks found.")

def add_task(t):
  temp = {}
  to_do = ""
  
  while not re.fullmatch(PATTERN_TASK, to_do): to_do = input("\nEnter task: ")

  temp["task"], temp["completed"] = "[ ] " + to_do, False
  t.append(temp)
  print("\nTask added successfully!")

def complete_task(t):
  length = len(t)
  if length > 0:
    view_tasks(t)
    c = get_number_of_task("\nChoose a task to complete: ", length)
    pos = c - 1
    if t[pos]["completed"] == True:
      print("\nTask already completed as completed!")
    else:
      t[pos]["completed"] = True
      print(f"\nTask '{t[pos]['task']}' marked as completed! ✓")
      t[pos]["task"] = t[pos]["task"].replace("[ ] ", "[✓] ")
  else:
    print("No tasks found")

def get_number_of_task(prompt, l):
  while True:
    try:
      n = int(input(prompt))
      end = l + 1
      if n not in range(1, end):
        print("\nChoose a number between the range of available choices!")
        continue
    except ValueError:
      continue
    break

  return n

def delete_task(t):
  length = len(t)
  if length > 0:
    view_tasks(t)
    c = get_number_of_task("\nChoose a task to complete: ", length)
    pos = c - 1
    t.pop(pos)
    print("\nTask deleted successfully!")
  else:
    print("\nNo tasks found")

main()
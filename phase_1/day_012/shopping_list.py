# Day 12 5/9/26!

import re

PATTERN_ITEM = r"[A-Za-z\s]+"
    
def main():
  print("=== Shopping List Manager ===")
  option = 0
  shopping_list = []
  while option != 6:
    option = get_number("\n1. View shopping list\n2. Add item\n3. Remove item\n4. Search item\n5. Clear list\n6. Exit\n\nChoose an option: ")
    match(option):
      case 1:
        length = len(shopping_list)
        if length != 0:
          print("=== Shopping List Manager ===\n")
          for i in range(len(shopping_list)):

            # Check if an item is being repeated in the list and print the number of times it is repeated, but only print the first instance of the item in the list
            if shopping_list[i].lower() not in [item.lower() for item in shopping_list[:i]]:
              count = sum(1 for item in shopping_list if item.lower() == shopping_list[i].lower())
              if count > 1:
                print(f"{i+1}. {shopping_list[i]} (x{count})")
              else:
                print(f"{i+1}. {shopping_list[i]}")
        else:
          print("\nYour shopping list is empty.")
      case 2:
        individual = add_item()
        if individual is not None:
            shopping_list.append(individual)
            print(f"\n'{individual}' added successfully!")
      case 3: remove_item(shopping_list)
      case 4: search_item(shopping_list)
      case 5: clear_list(shopping_list)

  print("Goodbye!")
        

def get_number(prompt):
  while True:
    try:
      n = int(input(prompt))
      if n not in [1,2,3,4,5,6]:
        print("Choose a number between 1 and 6\n")
        continue
    except ValueError:
      continue
    break

  return n

def add_item():
    i = ""

    while not re.fullmatch(PATTERN_ITEM, i): i = input("\nEnter item: ")

    return i

def remove_item(sl):
  while True:
    i = input("\nEnter item to remove: ")
    if re.fullmatch(PATTERN_ITEM, i):
      break

  pos = None
  for j in range(len(sl)):
    if i.lower() == sl[j].lower():
      pos = j
      break
    else:
      print(f"'{i}' not found in your shopping list.")
      return

  answer = ""
  while answer not in ["y", "n"]: answer = input("Are you sure? (y/n): ")
  if answer == "y":
      sl.pop(pos)
      print(f"'{i}' removed from your shopping list.")
  else: return

def search_item(sl):
  while True:
    i = input("\nSearch item: ")
    if re.fullmatch(PATTERN_ITEM, i): break

  count = 0
  for j in range(len(sl)):
    if i.lower() in sl[j].lower():
      count += 1
      print(f"Found '{sl[j]}' in your shopping list.")

  if count == 0: print("Not found")

def clear_list(sl):
  answer = ""
  while answer not in ["y", "n"]: answer = input("Are you sure you want to clear your shopping list? (y/n): ")
  if answer == "y":
      sl.clear()
      print("Your shopping list has been cleared.")
  else: return

main()
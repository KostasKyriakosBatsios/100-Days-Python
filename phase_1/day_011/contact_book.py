import re

PATTERN_NAME_FULL = r"[A-Za-z\s]+"
PATTERN_NAME = r"[A-Za-z]+"
PATTERN_PHONE = r"[0-9]+"
PATTERN_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def main():
  print("=== Contact Book ===")
  option = 0
  contacts = []
  while option != 6:
    option = get_number("\n1. Add contact\n2. View contacts\n3. Search contact\n4. Edit contact\n5. Delete contact\n6. Exit\n\nContact an option: ")
    match(option):
      case 1:
        name, phone, email = "", "", ""
        individual = add_contact(name, phone, email)
        contacts.append(individual)
        print("\nContact added successfully!")
      case 2:
        length = len(contacts)
        if length != 0:
          for i in range(len(contacts)):
            print(f"\n{i+1}.\t{contacts[i]["name"]}\n\tPhone: {contacts[i]["phone"]}\n\tEmail: {contacts[i]["email"]}")
        else:
          print("\nNo contacts found")
      case 3: search_contact(contacts)
      case 4: edit_contact(contacts)
      case 5: delete_contact(contacts)

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

def add_contact(n, p, e):
  c = {}
  
  while not re.fullmatch(PATTERN_NAME_FULL, n): n = input("\nName: ")

  while not re.fullmatch(PATTERN_PHONE, p): p = input("\nPhone: ")

  while not re.fullmatch(PATTERN_EMAIL, e): e = input("\nEmail: ")

  c["name"], c["phone"], c["email"] = n, p, e
  return c

def search_contact(con):
  while True:
    n = input("\nSearch: ").lower()
    if re.fullmatch(PATTERN_NAME, n): break

  count = 0
  for i in range(len(con)):
    if n in con[i]["name"].lower():
      count += 1
      print(f"Found:\n{i+1}.\t{con[i]["name"]}\n\tPhone: {con[i]["phone"]}\n\tEmail: {con[i]["email"]}")

  if count == 0: print("Not found")

def edit_contact(con):
  while True:
    n = input("\nEnter contact name: ").lower()
    if re.fullmatch(PATTERN_NAME_FULL, n): break

  pos = None
  for i in range(len(con)):
    if n == con[i]["name"].lower():
      pos = i
      break
    
  print(f"Current phone: {con[pos]["phone"]}")
  new_phone = ""
  while not re.fullmatch(PATTERN_PHONE, new_phone): new_phone = input("New phone: ")
    
  print(f"Current email: {con[pos]["email"]}")
  new_email = ""
  while not re.fullmatch(PATTERN_EMAIL, new_email): new_email = input("New email: ")
    
  con[pos]["phone"], con[pos]["email"] = new_phone, new_email

  return con

def delete_contact(con):
  while True:
    n = input("\nEnter contact name: ").lower()
    if re.fullmatch(PATTERN_NAME_FULL, n):
      break

  pos = None
  for i in range(len(con)):
    if n == con[i]["name"].lower():
      pos = i
      break

  answer = ""
  while answer not in ["y", "n"]: answer = input("Are you sure? (y/n): ")
  if answer == "y":
    if n == con[pos]["name"]:
      con.pop(pos)
      print("Contact deleted successfully!")
    else: print("Contact not found.")
  else: return

main()
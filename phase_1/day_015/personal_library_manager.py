# Day 15 10/9/26!

import json
import re

PATTERN_TITLE_AUTHOR = r"[A-Za-z\s]+"

def main():
  print("=== Personal Library Manager ===")

  # Load books from JSON file if exists, otherwise create an empty list
  try:
    with open("books.json", "r") as f:
      books = json.load(f)
  except FileNotFoundError:
    books = []
  option = ""
  
  while option != 6:
    option = get_number("\n1. View books\n2. Add book\n3. Search book\n4. Update reading status\n5. Delete book\n6. Exit\n\nChoose an option: ")
    match(option):
      case 1: 
        length = len(books)
        if length > 0:
          print("=== Your Library ===\n")
          
          for i in range(length):
            print(f"{i+1}. {books[i]['title']}\n Author: {books[i]['author']}\n Status: {books[i]['status']}\n")

        else:
          print("Your library is empty.")
            
      case 2: add_book(books)
      case 3: search_books(books)
      case 4: update_status(books)
      case 5: delete_book(books)

  print("Goodbye!")
  
def get_number(prompt):
  while True:
    try:
      n = int(input(prompt))
      if n not in [1,2,3,4,5,6]:
        print("Choose between 1 and 6")
        continue
    except ValueError:
      continue
    break

  return n

def add_book(b):
  temp = {}
  t, a, s = "", "", 0

  while not re.fullmatch(PATTERN_TITLE_AUTHOR, t): t = input("\nTitle: ")

  temp["title"] = t

  while not re.fullmatch(PATTERN_TITLE_AUTHOR, a): 
    a = input("Author: ")

    for i in range(len(b)):
      if t.lower() == b[i]["title"].lower():
        if a.lower() == b[i]["author"].lower():
          print("Book with that author already exists!")
          a = ""
          break

  while s not in [1,2,3]:
    try:
      s = int(input("Status:\n1. Want to Read\n2. Reading\n3. Completed\n\nChoose status: "))
    except ValueError:
      continue

  temp["author"] = a
  match(s):
    case 1: temp["status"] = "Want to Read"
    case 2: temp["status"] = "Reading"
    case 3: temp["status"] = "Completed"
  b.append(temp)
  print("Book added successfully!")

  # After adding a book, save the updated list to the JSON file
  save_books(b)

def search_books(b):
  text = ""
  
  while not re.fullmatch(PATTERN_TITLE_AUTHOR, text): text = input("\nSearch title or author: ")

  count = 0
  print("=== Search Results ===")
  for i in range(len(b)):
    if (text.lower() in b[i]["title"].lower()) or (text.lower() in b[i]["author"].lower()):
      count += 1
      print(f"\n{count}. {b[i]['title']}\n {b[i]['author']}\n {b[i]['status']}")

def update_status(b):
  ids = []
  print("=== Your Library ===")
  
  for i in range(len(b)):
    print(f"\n{i+1}. {b[i]['title']} by {b[i]['author']}")
    ids.append(i+1)

  n = 0

  while n not in ids:
    try:
      n = int(input("\nChoose book number: "))
    except ValueError:
      continue
  
  pos = n-1
  status, m = b[pos]['status'], 0
  while True:
    try:
      m = int(input(f"\nCurrent status: {status}\n\nChoose new status:\n\n1. Want to Read\n2. Reading\n3. Completed\n\nChoose: "))
      if m not in [1,2,3]:
        print("Choose 1,2 or 3")
        continue
    except ValueError:
      continue

    text = ""
    match(m):
      case 1: text = "Want to Read"
      case 2: text = "Reading"
      case 3: text = "Completed"

    if text == status:
      print("You chose a status that's already inserted")
    else:
      b[pos]['status'] = text
      break

  # After updating the status, save the updated list to the JSON file
  save_books(b)

def delete_book(b):
  ids = []
  print("=== Your Library ===")
  
  for i in range(len(b)):
    print(f"\n{i+1}. {b[i]['title']} by {b[i]['author']}")
    ids.append(i+1)

  n = 0
  
  while n not in ids:
    try:
      n = int(input("\nChoose book to delete: "))
    except ValueError:
      continue

  pos = n - 1
  answer = ""
  
  while answer not in ["y", "n"]: answer = input("\nAre you sure? (y/n): ").lower()

  if answer == "y":
    print(f"'{b[pos]['title']}' deleted successfully!")
    b.pop(pos)

  # After deleting a book, save the updated list to the JSON file
  save_books(b)

def save_books(b):
  with open("books.json", "w") as f:
    json.dump(b, f, indent=4)

main()
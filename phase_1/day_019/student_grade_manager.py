# Day 19 16/9/26!

import re

PATTERN_NAME = r"[A-Za-z\s]+"
PATTERN_GRADE = r"[0-9]{1,2}"

def main():
  print("=== STUDENT GRADE MANAGER ===\n")
  choice = 0
  students = []
  
  while choice != 7:
    choice = get_int("\n1. Add student\n2. View students\n3. Search student\n4. Calculate class average\n5. Show highest grade\n6. Show lowest grade\n7. Exit\n\nChoose one of the above options: ")
    match(choice):
      case 1: add_student(students)
      case 2: view_students(students)
      case 3: search_student(students)
      case 4: class_average(students)
      case 5: highest_grade(students)
      case 6: lowest_grade(students)

  print("Goodbye!")


def get_int(prompt):
  while True:
    try:
      n = int(input(prompt))
      if n not in [1,2,3,4,5,6,7]:
        print("Choose a number between 1 and 7")
        continue
    except ValueError:
      continue
    break

  return n

def add_student(s):
  temp = {}
  st, g = "", ""
  length = len(s)

  while not re.fullmatch(PATTERN_NAME, st): 
    st = input("\nEnter student name: ")
    if length > 0:
      for i in range(length):
        if st.lower() == s[i]["name"].lower():
          print("A student with that name exists. Give another name!")
          st = ""

  while not re.fullmatch(PATTERN_GRADE, g):
    g = input("Enter grade: ")
    g = int(g) if g.isdigit() else float(g)
    if 0 <= g <= 20: break
    else: 
      g = str(g)
      continue
    
  temp["name"], temp["grade"] = st, g
  s.append(temp)

def view_students(s):
  length = len(s)
  if length > 0:
    print("Students:\n")
    for i in range(length):
      print(f"{s[i]['name']} - {s[i]['grade']}")
    
  else: print("No students found.")

def search_student(s):
  st = ""

  while not re.fullmatch(PATTERN_NAME, st): st = input("\nEnter student name: ")

  pop = 0
  
  for i in range(len(s)):
    if st.lower() in s[i]["name"].lower():
      print(f"{s[i]['name']} - {s[i]['grade']}")
      pop += 1

  if pop == 0: print("Student not found.")

def class_average(s):
  sum, length = 0, len(s)

  for i in range(length):
    print(f"{s[i]['name']} - {s[i]['grade']}")
    sum += s[i]["grade"]

  print(f"\nClass average: {(sum / length):.2f}")

def highest_grade(s):
  max, pos = 0, 0

  for i in range(len(s)):
    if s[i]["grade"] > max: 
      max = s[i]["grade"]
      pos = i

  print(f"Highest grade: {max}\nStudent: {s[pos]['name']}")

def lowest_grade(s):
  min, pos = 20, 0

  for i in range(len(s)):
    if s[i]["grade"] < min: 
      min = s[i]["grade"]
      pos = i

  print(f"Lowest grade: {min}\nStudent: {s[pos]['name']}")

main()
# Day 39 14/10/26

import re

PATTERN_STRING = r"[A-Za-zΑ-Ζα-ζςΆΈΉΊΎΪΫάέήίύϊϋ0-9\s]+"

def main():
    print("=== LIBRARY MANAGEMENT SYSTEM ===")
    books = []
    
    while True:
        n = get_int("\n1. Show all books.\n2. Add book\n3. Search book\n4. Borrow book\n5. Return book\n6. Show available books\n7. Show borrowed books\n8. Library statistics\n9. Exit\n\nChoose: ")
        match(n):
            case 1:
                display_books(books)
            case 2:
                add_book(books)
            case 3:
                search_book(books)
            case 4:
                borrow_book(books)
            case 5:
                return_book(books)
            case 6:
                show_available_books(books)
            case 7:
                show_borrowed_books(books)
            case 8:
                statistics(books)
            case 9:
                break
    
    print("Goodbye!")
        
        
def get_int(p):
    while True:
        try:
            n = int(input(p))
            if (1 <= n <= 9):
                return n
            print("\nChoose between 1 and 9!")
        except ValueError:
            print("\nChoose a number!")
            continue

def display_books(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    print("\n=== ALL BOOKS ===\n")
    
    for temp in b:
        print(f"#{temp['id']} | {temp['title']} | {temp['author']} | {temp['category']} | {temp['status']}")

def add_book(b):
    b_id = 0 if check_emptiness(b) else len(b)
    t, a, c, dummy = "", "", "", {}
    
    while not re.fullmatch(PATTERN_STRING, t):
        t = input("\nTitle: ")
    
    while not re.fullmatch(PATTERN_STRING, a):
        a = input("Author: ")
    
    while not re.fullmatch(PATTERN_STRING, c):
        c = input("Category: ")
    
    if not check_emptiness(b):
        for temp in b:
            if t.lower() == temp["title"].lower() and a.lower() == temp["author"].lower():
                return print("\nBook with that title and author already in library!")
    
    dummy["id"], dummy["title"], dummy["author"], dummy["category"], dummy["status"] = b_id + 1, t, a, c, "Available"
    b.append(dummy)
    print("\nBook added successfully.")

def search_book(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    txt, flag = "", False
    
    while not re.fullmatch(PATTERN_STRING, txt):
        txt = input("\nSearch: ").lower()
    
    for temp in b:
        if (txt in temp["title"].lower()) or (txt in temp["author"].lower()):
            flag = True
            print(f"\n#{temp['id']} | {temp['title']} | {temp['author']} | {temp['category']} | {temp['status']}")
    
    if not flag:
        print("\nNo books found!")

def borrow_book(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    n = 0
    
    while True:
        try:
            n = int(input("\nEnter book id: "))
            if n > 0:
                break
            print("\nNumber must be positive.")
        except ValueError:
            print("\nMust be a number!")
            continue
    
    flag = False
        
    for temp in b:
        if n == temp["id"]:
            flag = True
            if temp["status"] == "Borrowed":
                return print("\nBook already borrowed.")
            else:
                temp["status"] = "Borrowed"
                return print("\nBook borrowed successfully.")
    
    if not flag:
        print("\nBook not found.")

def return_book(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    n = 0
    
    while True:
        try:
            n = int(input("\nEnter book id: "))
            if n > 0:
                break
            print("\nNumber must be positive.")
        except ValueError:
            print("\nMust be a number!")
            continue
    
    flag = False
    
    for temp in b:
        if n == temp["id"]:
            flag = True
            if temp["status"] == "Borrowed":
                temp["status"] = "Available"
                return print("\nBook returned successfully.")
            else:
                return print("\nBook is already available")
    
    if not flag:
        print("\nBook not found.")

def show_available_books(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    print("\n=== AVAILABLE BOOKS ===\n")
    
    for temp in b:
        if temp["status"] == "Available":
            print(f"#{temp['id']} | {temp['title']}")

def show_borrowed_books(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    print("\n=== BORROWED BOOKS ===\n")
    
    for temp in b:
        if temp["status"] == "Borrowed":
            print(f"#{temp['id']} | {temp['title']}")

def statistics(b):
    if check_emptiness(b):
        return print("\nNo books were found.")
    
    print("\n=== LIBRARY STATISTICS ===\n")
    total, count_a, count_b, count_c, dummy = 0, 0, 0, 0, []
    
    for temp in b:
        total += 1
        if temp["status"] == "Available":
            count_a += 1
        else:
            count_b += 1
        cat = temp["category"].lower()
        if cat not in dummy:
            dummy.append(cat)
            count_c += 1
    
    print(f"Total books: {total}\nAvailable: {count_a}\nBorrowed: {count_b}\nCategories: {count_c}")

def check_emptiness(b):
    return len(b) == 0

main()

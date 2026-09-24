import re

PATTERN_STRING = r"[A-Za-z\s]+"

def main():
    print("=== LIBRARY MANAGEMENT SYSTEM ===")
    books = [
        {"id": 1, "title": "The Odyssey", "author": "Homer", "category": "History", "status": "Available"},
        {"id": 2, "title": "Meditations", "author": "Marcus Aurelius", "category": "Philosophy", "status": "Borrowed"},
        {"id": 3, "title": "Python Course", "author": "Eric Matthes", "category": "Programming", "status": "Available"},
        {"id": 4, "title": "The Iliad", "author": "Homer", "category": "History", "status": "Available"},
        {"id": 5, "title": "The Apology", "author": "Plato", "category": "Philosophy", "status": "Available"},
        {"id": 6, "title": "Batman vs Superman", "author": "Zack Snyder", "category": "Action", "status": "Borrowed"}
    ]
    
    while True:
        n = get_int("\n1. Show all books.\n2. Add book\n3. Search book\n4. Borrow book\n5. Return book\n6. Show available books\n7. Show borrowed books\n8. Library statistics\n9. Exit\n\nChoose: ")
        match(n):
            case 1: display_books(books)
            case 2: add_book(books)
            case 3: search_book(books)
            case 4: borrow_book(books)
            case 5: return_book(books)
            case 6: show_available_books(books)
            case 7: show_borrowed_books(books)
            case 8: statistics(books)
            case _: break
    
    print("Goodbye!")
        
        
def get_int(p):
    while True:
        try:
            i = int(input(p))
            if not (1 <= i <= 9):
                continue
            break
        except ValueError:
            continue
        
    return i

def display_books(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    print("\n=== ALL BOOKS ===\n")
    
    for i in range(len(b)):
        print(f"#{b[i]['id']} | {b[i]['title']} | {b[i]['author']} | {b[i]['category']} | {b[i]['status']}")

def add_book(b):
    id = 0 if check_emptiness(b) else len(b)
    t, a, c= "", "", ""
    temp = {}
    
    while not re.fullmatch(PATTERN_STRING, t): t = input("\nTitle: ")
    
    while not re.fullmatch(PATTERN_STRING, a): a = input("Author: ")
    
    while not re.fullmatch(PATTERN_STRING, c): c = input("Category: ")
    
    temp["id"], temp["title"], temp["author"], temp["category"], temp["status"] = id + 1, t, a, c, "Available"
    b.append(temp)
    print("Book added successfully.\n")

def search_book(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    txt, flag = "", False
    
    while not re.fullmatch(PATTERN_STRING, txt): txt = input("\nSearch: ")
    
    print()
    
    for i in range(len(b)):
        if (txt.lower() in b[i]["title"].lower()) or (txt.lower() in b[i]["author"].lower()):
            flag = True
            print(f"#{b[i]['id']} | {b[i]['title']} | {b[i]['author']} | {b[i]['category']} | {b[i]['status']}")
    
    if not flag:
        print("No books found!")

    print()

def borrow_book(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    n = 0
    
    while True:
        try:
            n = int(input("\nEnter book id: "))
            if n <= 0:
                print("Number must be positive.")
                continue
            break
        except ValueError:
            continue
    
    flag = False
        
    for i in range(len(b)):
        if n == b[i]["id"]:
            if b[i]["status"] == "Borrowed":
                print("\nBook already borrowed.\n")
                return
            else:
                b[i]["status"] = "Borrowed"
                flag = True
                print("\nBook borrowed successfully.")
                return
    
    if not flag:
        print("\nBook not found.\n")

def return_book(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    n = 0
    
    while True:
        try:
            n = int(input("\nEnter book id: "))
            if n <= 0:
                print("Number must be positive.")
                continue
            break
        except ValueError:
            continue
    
    for i in range(len(b)):
        if n == b[i]["id"]:
            if b[i]["status"] == "Borrowed":
                b[i]["status"] = "Available"
                print("\nBook returned successfully.\n")
                return
            else:
                print("\nBook is already available")
                return

def show_available_books(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    print("\n=== AVAILABLE BOOKS ===\n")
    
    for i in range(len(b)):
        if b[i]["status"] == "Available":
            print(f"#{b[i]['id']} | {b[i]['title']}")
    
    print()

def show_borrowed_books(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    print("\n=== BORROWED BOOKS ===\n")
    
    for i in range(len(b)):
        if b[i]["status"] == "Borrowed":
            print(f"#{b[i]['id']} | {b[i]['title']}")
    
    print()

def statistics(b):
    if check_emptiness(b):
        return "No books were found.\n"
    
    print("\n=== LIBRARY STATISTICS ===\n")
    total, count_a, count_b, count_c = 0, 0, 0, 0
    temp = []
    
    for i in range(len(b)):
        total += 1
        if b[i]["status"] == "Available":
            count_a += 1
        else:
            count_b += 1
        if b[i]["category"] not in temp:
            temp.append(b[i]["category"])
            count_c += 1
    
    print(f"Total books: {total}\nAvailable: {count_a}\nBorrowed: {count_b}\nCategories: {count_c}")

def check_emptiness(b):
    return True if len(b) == 0 else False

main()

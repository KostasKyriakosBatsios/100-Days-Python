# Day 52 29/10/26

import re

PATTERN_TITLE = r"^(?=.*[a-zA-Z\s])[a-zA-Z0-9.\-?,\s]*$"
PATTERN_AUTHOR = r"[A-Za-z.\s]+"

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
    
    
    def display_info(self):
        print(f"\nBook ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nAvailable? {self.is_available}")
    
    
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        
        return False
    
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        
        return False


class Library:
    def __init__(self):
        self.books = []
    
    
    def add_book(self):
        b_id, t, a, y = len(self.books) + 1, "", "", 0
        
        while not re.fullmatch(PATTERN_TITLE, t):
            t = input("\nTitle: ")
        
        while not re.fullmatch(PATTERN_AUTHOR, a):
            a = input("\nAuthor: ")
        
        while True:
            try:
                y = int(input("\nYear: "))
                
                if y > 0:
                    break
                
                print("\nOnly positive integers.")
            except ValueError:
                print("\nOnly numbers")
        
        if self.books:
            for b in self.books:
                if t == b.title and a == b.author and y == b.year:
                    return print("\nThat book is already at the library!")
        
        self.books.append(Book(b_id, t, a, y))
        print("\nBook added successfully!")
    
    
    def display_books(self):
        if len(self.books) == 0:
            return print("\nNo books were found!")
        
        for b in self.books:
            b.display_info()
    
    
    def search_book(self):
        if len(self.books) == 0:
            return print("\nNo books were found!")
        
        txt, flag = "", False
        
        while not re.fullmatch(PATTERN_TITLE, txt):
            txt = input("\nEnter title or author: ")
        
        for b in self.books:
            if txt.lower() in b.title.lower() or txt.lower() in b.author.lower():
                flag = True
                b.display_info()
        
        if not flag:
            print(f"\nNo book with title or author {txt} was found!")
    
    
    def borrow_book(self):
        if len(self.books) == 0:
            return print("\nNo books were found!")
        
        b_id, flag_exist, flag_change = 0, False, False
        
        while True:
            try:
                b_id = int(input("\nBook ID: "))
                
                if b_id > 0:
                    break
                
                print("\nOnly positive integers!")
            except ValueError:
                print("\nOnly numbers!")
        
        for b in self.books:
            if b_id == b.book_id:
                flag_exist = True
                flag_change = b.borrow()
                if flag_change:
                    print("\nBook borrowed successfully!")
                else:
                    return print("\nThe book is already borrowed!")
        
        if not flag_exist:
            print(f"\nNo book with ID {b_id} was found!")
    
    
    def return_book(self):
        if len(self.books) == 0:
            return print("\nNo books were found!")
        
        b_id, flag_exist, flag_change = 0, False, False
        
        while True:
            try:
                b_id = int(input("\nBook ID: "))
                
                if b_id > 0:
                    break
                
                print("\nOnly positive integers!")
            except ValueError:
                print("\nOnly numbers!")
        
        for b in self.books:
            if b_id == b.book_id:
                flag_exist = True
                flag_change = b.return_book()
                if flag_change:
                    print("\nBook returned successfully")
                else:
                    print("\nThe book is already available!")
        
        if not flag_exist:
            print(f"\nNo book with ID {b_id} was found!")
    
    
    def display_available_books(self):
        if len(self.books) == 0:
            return print("\nNo books were found!")
        
        flag = False
        
        for b in self.books:
            if b.is_available:
                flag = True
                b.display_info()
        
        if not flag:
            print("\nNo book is available!")


def main():
    print("========== LIBRARY SYSTEM ==========")
    
    lib = Library()
    
    while True:
        num = get_num("\n1. Add book\n2. Display all books\n3. Search book\n4. Borrow book\n5. Return book\n6. Display available books\n7. Exit\n\nChoose: ")
        
        match(num):
            case 1:
                lib.add_book()
            case 2:
                lib.display_books()
            case 3:
                lib.search_book()
            case 4:
                lib.borrow_book()
            case 5:
                lib.return_book()
            case 6:
                lib.display_available_books()
            case 7:
                break
    
    print("\nGoodbye!")


def get_num(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 7:
                return n
            
            print("\nOnly integers between 1 and 7.")
        except ValueError:
            print("\nOnly numbers!")


main()

# Day 48 26/10/26

import json
import re

PATTERN_NAME = r"[A-Za-z\s]+"
PATTERN_PHONE = r"[\+0-9]{10,13}"
PATTERN_EMAIL = r"[A-Za-z0-9]+@[\w]+\.[\w]+"

class Contact:
    def __init__(self, c_id, name, phone, email):
        self.c_id = c_id
        self.name = name
        self.phone = phone
        self.email = email
    
    
    def c_display(self):
        print(f"\nID: {self.c_id}\nName: {self.name}\nPhone: {self.phone}\nEmail: {self.email}")
    

class ContactBook:
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts is not None else []
        
        for c in self.contacts:
            c_obj = Contact(c['c_id'], c['name'], c['phone'], c['email'])
            self.contacts[self.contacts.index(c)] = c_obj
    
    
    def add_contact(self):
        c_id, n, p, e = len(self.contacts) + 1, "", "", ""
        
        if c_id != 0:
            for c in self.contacts:
                if c_id == c.c_id:
                    c_id += 1
        
        while not re.fullmatch(PATTERN_NAME, n):
            n = input("\nName: ")
        
        while not re.fullmatch(PATTERN_PHONE, p):
            p = input("\nPhone: ")
        
        while not re.fullmatch(PATTERN_EMAIL, e):
            e = input("\nEmail: ")
        
        temp = Contact(c_id, n, p, e)
        self.contacts.append(temp)
        print("\nContact has been added successfully")
    
    
    def display_contacts(self):
        if len(self.contacts) == 0:
            return print("\nNo contacts found!")
        
        for c in self.contacts:
            c.c_display()
    
    
    def search_name_contact(self):
        if len(self.contacts) == 0:
            return print("\nNo contacts found!")
        
        n, flag = "", False
        
        while not re.fullmatch(PATTERN_NAME, n):
            n = input("\nName: ")
        
        for c in self.contacts:
            if n.lower() == c.name.lower():
                flag = True
                c.c_display()
        
        if not flag:
            print(f"No contact with name {n} was found!")
    
    
    def search_number_contact(self):
        if len(self.contacts) == 0:
            return print("\nNo contacts found!")
        
        p, flag = "", False
        
        while not re.fullmatch(PATTERN_PHONE, p):
            p = input("\nPhone: ")
        
        for c in self.contacts:
            if p == c.phone:
                flag = True
                c.c_display()
            
        if not flag:
            print(f"No contact with number {p} was found!")
    
    
    def update_contact_info(self):
        if len(self.contacts) == 0:
            return print("\nNo contacts found!")
        
        n, flag = "", False
        
        while not re.fullmatch(PATTERN_NAME, n):
            n = input("\nName: ")
        
        for c in self.contacts:
            if n.lower() == c.name.lower():
                flag = True
                c_id, nm, p, e = change_info(c)
                c.c_id = c_id
                c.name = nm
                c.phone = p
                c.email = e
        
        if not flag:
            return print(f"\nNo contact with name {n} was found to change!")
        
        print("\nContact changed successfully!")
    
    
    def delete_contact(self):
        if len(self.contacts) == 0:
            return print("\nNo contacts found!")
        
        c_id, flag = 0, False
        
        while True:
            try:
                c_id = int(input("\nID: "))
                
                if c_id > 0:
                    break
                
                print("\nOnly positive integer numbers!")
            except ValueError:
                print("\nOnly numbers!")
                continue
    
        for c in self.contacts:
            if c_id == c.c_id:
                flag = True
                temp = c
        
        if not flag:
            return print(f"\nNo user with ID {c_id} was found!")
        
        ch = ""
        
        while ch not in ['y', 'n']:
            ch = input("Are you sure you want to delete this contact? [y/n]\n-").lower()
        
        if ch == 'n':
            return print("\nOK. The contact will not be deleted!")
        
        self.contacts.remove(temp)
        print("\nThe contact was removed successfully!")
    
    
    def save(self):
        with open('contacts.json', 'w') as f:
            json.dump([vars(c) for c in self.contacts], f, indent=4)


def main():
    print("\n========== CONTACT BOOK ==========")
    
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    
    cb_obj = ContactBook(contacts)
    
    while True:
        number = get_number("\n1. Add contact\n2. Display all contacts\n3. Search contact based on name\n4. Search contact based on phone number\n5. Update contact info\n6. Delete contact\n7. Exit\n\nChoose: ")
        
        match(number):
            case 1:
                cb_obj.add_contact()
            case 2:
                cb_obj.display_contacts()
            case 3:
                cb_obj.search_name_contact()
            case 4:
                cb_obj.search_number_contact()
            case 5:
                cb_obj.update_contact_info()
            case 6:
                cb_obj.delete_contact()
            case 7:
                cb_obj.save()
                break
    
    print("\nGoodbye!")


def get_number(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 7:
                return n
                
            print("\nOnly integers between 1 and 7.")
        except ValueError:
            print("\nOnly numbers!")
            continue


def change_info(c):
    c_id, n, p, e = c.c_id, "", "", ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nNew Name: ")
    
    while not re.fullmatch(PATTERN_PHONE, p):
        p = input("\nNew Phone: ")
    
    while not re.fullmatch(PATTERN_EMAIL, e):
        e = input("\nNew Email: ")
    
    return c_id, n, p, e


main()

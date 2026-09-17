# Day 20 17/9/26!

import re 

PATTERN_NAME = r"[A-Za-z\s]+"
PATTERN_PRICE = r"[0-9]+\.[0-9]{1,2}"
PATTERN_QUANTITY = r"[0-9]+"

def main():
    print("=== INVENTORY MANAGEMENT ===")
    choice = 0
    products = []
    while choice != 7:
        choice = get_int("\n1. Add product\n2. View products\n3. Search product\n"
        "4. Update stock\n5. Remove product\n6. Calculate inventory value\n7. Exit\n\nChoose: ")
        match(choice):
            case 1: add_products(products)
            case 2: view_products(products)
            case 3: search_product(products)
            case 4: update_stock(products)
            case 5: remove_product(products)
            case 6: calculate_inventory_value(products)
            
    
    print("Goodbye")

def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n not in [1,2,3,4,5,6,7]:
                print("Choose between options 1 and 7.")
                continue
        except ValueError:
            continue
        break
    
    return n

def add_products(p):
    temp = {}
    length = len(p)
    n, pr, q = "", "", ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nEnter product name: ")
        if length > 0:
            for i in range(length):
                if n.lower() == p[i]["name"].lower():
                    print("A product with that name already exists.")
                    n = ""
                    break
    
    while not re.fullmatch(PATTERN_PRICE, pr): pr = input("Enter price: ")
    
    pr = float(pr)
    
    while not re.fullmatch(PATTERN_QUANTITY, q): q = input("Enter quantity: ")
    
    q = int(q)
    temp["name"], temp["price"], temp["quantity"] = n, pr, q
    p.append(temp)
    
def view_products(p):
    length = len(p)
    if length > 0:
        print("Products:\n")
        for i in range(length):
            print(f"{p[i]['name']} - €{p[i]['price']} - Stock: {p[i]['quantity']}")
    else:
        print("Inventory is empty")

def search_product(p):
    has_size = check_list_size(p)
    if has_size:
        return
    
    n = ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nEnter product name: ")
    
    count = 0
    
    for i in range(len(p)):
        if n.lower() in p[i]["name"].lower():
            print(f"{p[i]['name']} - €{p[i]['price']} - Stock: {p[i]['quantity']}")
            count += 1
    
    if count == 0:
        print("Product not found.")

def update_stock(p):
    has_size = check_list_size(p)
    if has_size:
        return
    
    n, q = "", ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nEnter product name: ")
    
    pos = -1
    
    for i in range(len(p)):
        if n.lower() == p[i]["name"].lower():
            pos = i
    
    if pos == -1:
        print("Couldn't find the product to restock it.")
        return
    
    while not re.fullmatch(PATTERN_QUANTITY, q):
        q = input("Enter new quantity: ")
    
    q = int(q)
    p[pos]["quantity"] = q
    print("Stock updated successfully.")

def remove_product(p):
    has_size = check_list_size(p)
    if has_size:
        return
    
    n = ""
    
    while not re.fullmatch(PATTERN_NAME, n):
        n = input("\nEnter product name: ")
    
    pos = -1
    
    for i in range(len(p)):
        if n.lower() == p[i]["name"].lower():
            pos = i
    
    if pos == -1:
        print("Couldn't find the product to remove it.")
        return
    
    print(f"{p[pos]['name']} removed successfully.")
    p.remove(p[pos])

def calculate_inventory_value(p):
    has_size = check_list_size(p)
    if has_size:
        return
    
    total = 0
    
    for i in range(len(p)):
        multiply = p[i]['price'] * p[i]['quantity']
        print(f"{p[i]['name']}: {p[i]['price']} x {p[i]['quantity']} = {multiply:.2f}")
        total += multiply
    
    print(f"Total inventory value: €{total:.2f}")

def check_list_size(p):
    length = len(p)
    if length == 0:
        print("Inventory is empty.")
        return True
    
    return False

main()

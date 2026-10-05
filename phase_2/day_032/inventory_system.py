# Day 32 5/10/26

import re

PATTERN_STRING = r"[A-Za-z\s]+"

class Product:
    def __init__(self, id, name, price, quantity, category):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category}")
    
    def sell(self, quantity_sell):
        self.quantity -= quantity_sell
    
    def restock(self, quantity_restock):
        self.quantity += quantity_restock
    
    def get_total_value(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def show_products(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        for product in self.products:
            product.display()
    
    def add_product(self):
        id, nm, pr, q, c = 0, "", 0, -1, ""
        
        while True:
            try:
                id = int(input("\nID: "))
                if len(self.products) == 0 and not id <= 0:
                    break
                
                if id <= 0:
                    continue
                else:
                    flag = True
                    
                    for product in self.products:
                        if id == product.id:
                            print(f"\nProduct {id} already exists")
                            flag = False
                            break
                    
                    if flag:
                        break
                
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        while pr <= 0.0:
            try:
                pr = float(input("Price: "))
            except ValueError:
                continue
        
        while q < 0:
            try:
                q = int(input("Quantity: "))
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_STRING, c):
            c = input("Category: ")
        
        p = Product(id, nm, pr, q, c)
        self.products.append(p)
    
    def find_product(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        id = 0
        
        while id <= 0:
            try:
                id = int(input("\nID: "))
            except ValueError:
                continue
        
        flag = False
        
        for product in self.products:
            if id == product.id:
                product.display()
                flag = True
        
        if not flag:
            print(f"\nProduct {id} wasn't on the inventory.")
    
    def search_products(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        nm = ""
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("\nName: ")
        
        flag = False
        
        for product in self.products:
            if nm.lower() in product.name.lower():
                product.display()
                flag = True
        
        if not flag:
            print(f"\nProduct '{nm}' wasn't on the inventory.")
    
    def sell_product(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        id, q = 0, 0
        
        while id <= 0:
            try:
                id = int(input("\nProduct ID: "))
                
                flag = False
                
                for product in self.products:
                    if id == product.id:
                        flag = True
                
                if not flag:
                    return print(f"\nProduct {id} wasn't on inventory.")
                        
            except ValueError:
                continue
        
        while q <= 0:
            try:
                q = int(input("Quantity: "))
                
                for product in self.products:
                    if q > product.quantity:
                        print("\nThe number cannot be larger than the available number on the inventory.")
                        q = 0
                
            except ValueError:
                continue
        
        for product in self.products:
            if id == product.id:
                product.sell(q)
    
    def restock_product(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        id, q = 0, 0
        
        while id <= 0:
            try:
                id = int(input("\nProduct ID: "))
                
                flag = False
                
                for product in self.products:
                    if id == product.id:
                        flag = True
                
                if not flag:
                    return print(f"\nProduct {id} wasn't on inventory.")
                        
            except ValueError:
                continue
        
        while q <= 0:
            try:
                q = int(input("Quantity: "))
            except ValueError:
                continue
        
        for product in self.products:
            if id == product.id:
                product.restock(q)
    
    def show_low_stock(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        theta = 0
        
        while theta <= 0:
            try:
                theta = int(input("\nLow stock threshold: "))
            except ValueError:
                continue
        
        flag = False
        
        for product in self.products:
            if product.quantity <= theta:
                product.display()
                flag = True
        
        if not flag:
            print(f"\nNo products are below the threshold {theta}")
    
    def statistics(self):
        if len(self.products) == 0:
            return print("\nNo products were found!")
        
        total_p, total_q, total_value, max_price, max_stock = 0, 0, 0, 0, 0
        
        for product in self.products:
            total_p += 1
            total_q += product.quantity
            total_value += product.get_total_value()
            if product.price >= max_price:
                max_price = product.price
            if product.quantity >= max_stock:
                max_stock = product.quantity
        
        print(f"\nTotal products: {total_p}\nTotal quantity of items: {total_q}\nTotal inventory value: {total_value}\nMost expensive product: {max_price}\nProduct with the highest stock: {max_stock}")

def main():
    print("========== INVENTORY SYSTEM ==========")
    inventory = Inventory()
    
    while True:
        num = get_int("\nChoose between 1 and 9: ")
        match(num):
            case 1: inventory.show_products()
            case 2: inventory.add_product()
            case 3: inventory.find_product()
            case 4: inventory.search_products()
            case 5: inventory.sell_product()
            case 6: inventory.restock_product()
            case 7: inventory.show_low_stock()
            case 8: inventory.statistics()
            case 9: break
    
    print("\nGoodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            return n if (1 <= n <= 9) else print("\nNumber must be between 1 and 9")
        except ValueError:
            continue

main()

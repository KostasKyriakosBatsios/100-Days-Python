import re

PATTERN_STRING = r"[A-Za-z\s]+"

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def display(self):
        print(f"\nID: {self.id}\nProduct: {self.name}\nPrice: {self.price}\nStock: {self.stock}")
    
    def sell(self, quantity):
        self.stock -= quantity
    
    def restock(self, quantity):
        self.stock += quantity

class Customer:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance
    
    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nBalance: {self.balance}")
    
    def pay(self, amount):
        self.balance -= amount

class Store:
    def __init__(self):
        self.products = []
        self.customers = []
    
    def show_products(self):
        if check_length(self.products):
            print("No products found")
            return
        
        for i in range(len(self.products)):
            self.products[i].display()
    
    def add_product(self):
        length = len(self.products)
        pid, nm, pr, st = 0, "", 0.0, 0
        
        while pid == 0:
            try:
                pid = int(input("Product ID: "))
            except ValueError:
                continue
            if length == 0:
                break
            
            for i in range(length):
                if pid == self.products[i].id:
                    print("Product with that id already exists!")
                    pid = 0
                    continue
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        while pr == 0.0:
            try:
                pr = float(input("Price: "))
            except ValueError:
                continue
        
        while st == 0:
            try:
                st = int(input("Stock: "))
            except ValueError:
                continue
        
        product = Product(pid, nm, pr, st)
        self.products.append(product)
            
    
    def find_product(self):
        if check_length(self.products):
            print("No products found")
            return
        
        pid = 0
        
        while pid == 0:
            try:
                pid = int(input("Product ID: "))
            except ValueError:
                continue
        
        flag = False
        
        for i in range(len(self.products)):
            if pid == self.products[i].id:
                self.products[i].display()
                flag = True
        
        if not flag:
            print(f"No product {pid} was found")
                
    
    def show_customers(self):
        if check_length(self.customers):
            print("No customers found")
            return
        
        for i in range(len(self.customers)):
            self.customers[i].display()
    
    def add_customer(self):
        length = len(self.customers)
        cid, nm, bl = 0, "", 0.0
        
        while cid == 0:
            try:
                cid = int(input("Customer ID: "))
            except ValueError:
                continue
            if length == 0:
                break
            
            for i in range(length):
                if cid == self.customers[i].id:
                    print("Customer with that id already exists!")
                    cid = 0
                    continue
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        while bl == 0.0:
            try:
                bl = float(input("Balance: "))
            except ValueError:
                continue
        
        customer = Customer(cid, nm, bl)
        self.customers.append(customer)
    
    def find_customer(self):
        if check_length(self.customers):
            print("No customers found")
            return
        
        cid = 0
        
        while cid == 0:
            try:
                cid = int(input("Customer ID: "))
            except ValueError:
                continue
        
        flag = False
        
        for i in range(len(self.customers)):
            if cid == self.customers[i].id:
                self.customers[i].display()
                flag = True
        
        if not flag:
            print(f"No customer {cid} was found.")
    
    def buy_product(self):
        if check_length(self.products):
            print("No products found")
            return
    
        pos_cid, pos_pid = -1, -1
        
        while True:
            try:
                cid = int(input("Customer ID: "))
            except ValueError:
                continue
            
            for i in range(len(self.customers)):
                if cid == self.customers[i].id:
                    pos_cid = i
                    break
            
            if pos_cid >= 0:
                break
        
        while True:
            try:
                pid = int(input("Product ID: "))
            except ValueError:
                continue
            
            for i in range(len(self.products)):
                if pid == self.products[i].id:
                    pos_pid = i
                    break
            
            if pos_pid >= 0:
                break
        
        qu, total = 0, 0
        
        while qu == 0:
            try:
                qu = int(input("Quantity: "))
            except ValueError:
                continue
            if qu > self.products[pos_pid].stock:
                print("Quantity cannot be larger than the available stock!")
                qu = 0
            total = self.products[pos_pid].price * qu
            if total > self.customers[pos_cid].balance:
                print(f"The customer {cid} doesn't have enough money")
                return 0
        
        
        self.customers[pos_cid].pay(total)
        self.products[pos_pid].sell(qu)
            
    
    def restock_product(self):
        if check_length(self.products):
            print("No products found")
            return
    
        pos_pid, qu = -1, 0
        
        while True:
            try:
                pid = int(input("Product ID: "))
            except ValueError:
                continue
            
            for i in range(len(self.products)):
                if pid == self.products[i].id:
                    pos_pid = i
                    break
            
            if pos_pid >= 0:
                break
        
        while qu == 0:
            try:
                qu = int(input("Quantity: "))
            except ValueError:
                continue
        
        self.products[pos_pid].restock(qu)
            
    
    def statistics(self):
        if check_length(self.products):
            print("No products found")
            return
        total_p, total_c, count_s, inv_value = 0, 0, 0, 0
        
        for i in range(len(self.products)):
            total_p += 1
            if self.products[i].stock != 0:
                count_s += 1
            inv_value += self.products[i].price * self.products[i].stock
        
        for i in range(len(self.customers)):
            total_c += 1
        
        print(f"\nTotal products: {total_p}\nTotal customers: {total_c}\n")

def main():
    print("========== ONLINE STORE ==========")
    store = Store()
    
    while True:
        num = get_int("\n1. Show products\n2. Add product\n3. Find product\n4. Show customers\n5. Add customer\n6. Find customer\n7. Buy product\n8. Restock product\n9. Show statistics\n10. Exit\n\nChoose: ")
        match(num):
            case 1: store.show_products()
            case 2: store.add_product()
            case 3: store.find_product()
            case 4: store.show_customers()
            case 5: store.add_customer()
            case 6: store.find_customer()
            case 7: store.buy_product()
            case 8: store.restock_product()
            case 9: store.statistics()
            case 10: break
    
    print("Goodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            if not (1 <= n <= 10):
                continue
            break
        except ValueError:
            continue
    
    return n

def check_length(temp):
    if len(temp) == 0:
        return True
    return False

main()

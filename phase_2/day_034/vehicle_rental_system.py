# Day 34 7/10/26

import re

PATTERN_STRING = r"[A-Za-z\s]+"
PATTERN_MODEL = r"[A-Za-z0-9\s]+"

class Vehicle:
    def __init__(self, id, brand, model, daily_rate):
        self.id = id
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.available = True
    
    def display(self):
        print(f"\nID: {self.id}\nBrand: {self.brand}\nModel: {self.model}"
        f"\nDaily rate: {self.daily_rate}\nAvailable: {self.available}")
    
    def calculate_rental_cost(self, days):
        return self.daily_rate * days
    
    def rent(self):
        self.available = False
    
    def return_vehicle(self):
        self.available = True

class Car(Vehicle):
    def __init__(self, id, brand, model, daily_rate, doors):
        super().__init__(id, brand, model, daily_rate)
        self.doors = doors
    
    def display(self):
        super().display()
        print(f"Doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, id, brand, model, daily_rate, engine_cc):
        super().__init__(id, brand, model, daily_rate)
        self.engine_cc = engine_cc
    
    def display(self):
        super().display()
        print(f"Engine CC: {self.engine_cc}")

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rented_vehicle = None
    
    def display(self):
        if self.rented_vehicle is not None:
            print(f"\nID: {self.id}\nName: {self.name}\nRented vehicle:")
            self.rented_vehicle.display()
        else:
            print(f"\nID: {self.id}\nName: {self.name}\nRented vehicle: {self.rented_vehicle}")
    
    def rent_vehicle(self, vehicle):
        self.rented_vehicle = vehicle
    
    def return_vehicle(self):
        self.rented_vehicle = None

class RentalSystem:
    def __init__(self):
        self.vehicles, self.customers = [], []
    
    def add_vehicle(self):
        o = 0
        
        while True:
            try:
                o = int(input("\n1. Car\n2. Motorcycle\n\nChoose: "))
                if o in [1,2]:
                    break
            except ValueError:
                continue
            
        id, br, md, dr = 0, "", "", 0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
                if (len(self.vehicles) == 0) and id != 0:
                    break
                
                flag = True
                
                for v in self.vehicles:
                    if id == v.id:
                        print(f"\nVehicle {id} already exists!")
                        id, flag = 0, False
                        break
                
                if not flag:
                    continue
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_STRING, br):
            br = input("Brand: ")
        
        while not re.fullmatch(PATTERN_MODEL, md):
            md = input("Model: ")
        
        while dr == 0:
            try:
                dr = abs(int(input("Daily rate: ")))
            except ValueError:
                continue
        
        match(o):
            case 1:
                d = 0
                
                while d == 0:
                    try:
                        d = abs(int(input("Doors: ")))
                    except ValueError:
                        continue
                
                temp = Car(id, br, md, dr, d)
            case 2:
                e = 0
                
                while e == 0:
                    try:
                        e = abs(int(input("Engine CC: ")))
                    except ValueError:
                        continue
                
                temp = Motorcycle(id, br, md, dr, e)
        self.vehicles.append(temp)
        
    
    def add_customer(self):
        id, nm = 0, ""
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
                if (len(self.customers) == 0) and id != 0:
                    break
                
                flag = True
                
                for c in self.customers:
                    if id == c.id:
                        print(f"\nCustomer {id} already exists!")
                        id, flag = 0, False
                        break
                
                if not flag:
                    continue
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        temp = Customer(id, nm)
        self.customers.append(temp)
    
    def show_vehicles(self):
        if len(self.vehicles) == 0:
            return print("\nNo vehicles found!")
        
        for v in self.vehicles:
            v.display()
        
    def show_customers(self):
        if len(self.customers) == 0:
            return print("\nNo customers found!")
        
        for c in self.customers:
            c.display()
    
    def show_available_vehicles(self):
        if len(self.vehicles) == 0:
            return print("\nNo vehicles found!")
        
        for v in self.vehicles:
            if v.available:
                v.display()
    
    def find_vehicle(self):
        if len(self.vehicles) == 0:
            return print("\nNo vehicles found!")
        
        id = 0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        flag = False
        
        for v in self.vehicles:
            if id == v.id:
                v.display()
                flag = True
        
        if not flag:
            print(f"\nVehicle {id} not found.")
    
    def find_customer(self):
        if len(self.customers) == 0:
            return print("\nNo customers found!")
        
        id = 0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        flag = False
        
        for c in self.customers:
            if id == c.id:
                c.display()
                flag = True
        
        if not flag:
            print(f"\nCustomer {id} not found.")
    
    def rent_vehicle(self):
        if (len(self.customers) == 0) and (len(self.vehicles) == 0):
            return print("\nNo vehicles and/or customers found!")
        
        c_id, v_id, d, pos_c, pos_v = 0, 0, 0, 0, 0
        
        while True:
            try:
                c_id = abs(int(input("\nCustomer ID: ")))
                
                flag = False
                
                for i, c in enumerate(self.customers):
                    if (c_id == c.id) and (not c_id == 0):
                        flag, pos_c = True, i
                        break
                
                if flag:
                    break
            except ValueError:
                continue
        
        while True:
            try:
                v_id = abs(int(input("Vehicle ID: ")))
                
                flag = False
                
                for i, v in enumerate(self.vehicles):
                    if (v_id == v.id) and (not v_id == 0):
                        flag, pos_v = True, i
                        break
                
                if flag:
                    break
            except ValueError:
                continue
        
        while d == 0:
            try:
                d = abs(int(input("Days: ")))
            except ValueError:
                continue
        
        c, v = self.customers[pos_c], self.vehicles[pos_v]
        if (c.rented_vehicle is None) and v.available:
            v.rent()
            c.rent_vehicle(v)
            print(f"All set. Rental cost: {v.calculate_rental_cost(d)}")
        else:
            print(f"\nCustomer {c_id} is renting a vehicle and/or the vehicle {v_id} isn't available.")
    
    def return_vehicle(self):
        if len(self.customers) == 0:
            return print("\nNo customers found!")
        
        c_id, pos_c = 0, 0
        
        while True:
            try:
                c_id = abs(int(input("\nCustomer ID: ")))
                
                flag = False
                
                for i, c in enumerate(self.customers):
                    if (c_id == c.id) and (not c_id == 0):
                        flag, pos_c = True, i
                        break
                
                if flag:
                    break
            except ValueError:
                continue
        
        c = self.customers[pos_c]
        if c.rented_vehicle is not None:
            c.rented_vehicle.return_vehicle()
            c.return_vehicle()
        else:
            print(f"\nCustomer {c_id} is not renting a vehicle!")
    
    def show_statistics(self):
        if (len(self.customers) == 0) and (len(self.vehicles) == 0):
            return print("\nNo vehicles and/or customers found!")
        
        total_v, av_v, ren_v, total_c, max_dr, sum = len(self.vehicles), 0, 0, len(self.customers), 0, 0
        
        for v in self.vehicles:
            dr = v.daily_rate
            sum += dr
            if v.available:
                av_v += 1
            else:
                ren_v += 1
            if dr > max_dr:
                max_dr = dr
            
        print(f"Total vehicles: {total_v}\nAvailable vehicles: {av_v}\nRented vehicles: {ren_v}"
        f"\nTotal customers: {total_c}\nMost expensive vehicle: {max_dr}"
        f"\nAverage daily rental rate: {(sum/total_v):.2f}")

def main():
    print("====== VEHICLE RENTAL SYSTEM ======")
    sys = RentalSystem()
    
    while True:
        num = get_int("\n1. Show vehicles\n2. Add vehicle\n3. Show available vehicles\n4. Find vehicle"
        "\n5. Show customers\n6. Add customer\n7. Find customer\n8. Rent vehicle\n9. Return vehicle"
        "\n10. Show statistics\n11. Exit\n\nChoose: ")
        match(num):
            case 1:
                sys.show_vehicles()
            case 2:
                sys.add_vehicle()
            case 3:
                sys.show_available_vehicles()
            case 4:
                sys.find_vehicle()
            case 5:
                sys.show_customers()
            case 6:
                sys.add_customer()
            case 7:
                sys.find_customer()
            case 8:
                sys.rent_vehicle()
            case 9:
                sys.return_vehicle()
            case 10:
                sys.show_statistics()
            case 11:
                break
    
    print("\nGoodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            return n if (1 <= n <= 11) else print("\nChoose between 1 and 11!")
        except ValueError:
            continue

main()

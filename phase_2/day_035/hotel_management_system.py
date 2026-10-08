# Day 35 8/10/26

import re

class Room:
    def __init__(self, id, number, daily_rate):
        self.id = id
        self.number = number
        self.daily_rate = daily_rate
        self.available = True
    
    def display(self):
        print(f"\nID: {self.id}\nNumber: {self.number}\nDaily rate: {self.daily_rate}\nAvailable: {self.available}")
    
    def calculate_cost(self, days):
        return self.daily_rate * days
    
    def book(self):
        self.available = False
    
    def checkout(self):
        self.available = True

class SingleRoom(Room):
    def __init__(self, id, number, daily_rate):
        super().__init__(id, number, daily_rate)
        self.bed_type = "Single"
    
    def display(self):
        super().display()
        print(f"Bed type: {self.bed_type}")

class DoubleRoom(Room):
    def __init__(self, id, number, daily_rate):
        super().__init__(id, number, daily_rate)
        self.beds = 2
    
    def display(self):
        super().display()
        print(f"Number of beds: {self.beds}")

class Guest:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.booked_room = None
    
    def display(self):
        if self.booked_room is None:
            print(f"\nID: {self.id}\nName: {self.name}\nBooked room: {self.booked_room}")
        else:
            print(f"\nID: {self.id}\nName: {self.name}\nBooked room:")
            self.booked_room.display()
    
    def book_room(self, room):
        self.booked_room = room
    
    def checkout(self):
        self.booked_room = None

class Hotel:
    def __init__(self):
        self.rooms, self.guests = [], []
    
    def show_rooms(self):
        if len(self.rooms) == 0:
            return print("\nNo rooms found!")
        
        for r in self.rooms:
            r.display()
    
    def add_room(self):
        o = 0
        
        while o == 0:
            try:
                o = abs(int(input("\n1. Single\n2. Double\n\nChoose: ")))
                if o not in [1,2]:
                    print("\nChoose between 1 and 2.")
                    o = 0
            except ValueError:
                continue
        
        id, n, dr = 0, 0, 0.0
        
        while True:
            try:
                id = abs(int(input("\nID: ")))
                if (len(self.rooms) == 0) and id != 0:
                    break
                
                flag = True
                
                for r in self.rooms:
                    if id == r.id:
                        print(f"\nRoom ID {id} already exists!")
                        id, flag = 0, False
                        break
                
                if flag and id != 0:
                    break
            except ValueError:
                continue
        
        while True:
            try:
                n = abs(int(input("\nNumber: ")))
                if (len(self.rooms) == 0) and n != 0:
                    break
                
                flag = True
                
                for r in self.rooms:
                    if n == r.number:
                        print(f"\nRoom number {n} already exists!")
                        n, flag = 0, False
                        break
                
                if flag and n != 0:
                    break
            except ValueError:
                continue
        
        while dr == 0.0:
            try:
                dr = abs(float(input("\nDaily rate: ")))
            except ValueError:
                continue
        
        if o == 1:
            temp = SingleRoom(id, n, dr)
        else:
            temp = DoubleRoom(id, n, dr)
        self.rooms.append(temp)
            
    def show_available_rooms(self):
        if len(self.rooms) == 0:
            return print("\nNo rooms found!")
        
        for r in self.rooms:
            if r.available:
                r.display()
    
    def find_room(self):
        if len(self.rooms) == 0:
            return print("\nNo rooms found!")
        id = 0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        flag = False
        
        for r in self.rooms:
            if id == r.id:
                r.display()
                flag = True
        
        if not flag:
            print(f"\nRoom ID {id} not found.")
    
    def show_guests(self):
        if len(self.guests) == 0:
            return print("\nNo guests found!")
        
        for g in self.guests:
            g.display()
    
    def add_guest(self):
        id, nm = 0, ""
        
        while True:
            try:
                id = abs(int(input("\nID: ")))
                if (len(self.guests) == 0) and id != 0:
                    break
                
                flag = True
                
                for g in self.guests:
                    if id == g.id:
                        print(f"\nGuest {id} already exists!")
                        id, flag = 0, False
                        break
                
                if flag and id != 0:
                    break
            except ValueError:
                continue
        
        while not re.fullmatch(r"[A-Za-z\s]+", nm):
            nm = input("\nName: ")
        
        self.guests.append(Guest(id, nm))
    
    def find_guest(self):
        if len(self.guests) == 0:
            return print("\nNo guests found!")
        id = 0
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        flag = False
        
        for g in self.guests:
            if id == g.id:
                g.display()
                flag = True
        
        if not flag:
            print(f"\nGuest {id} not found!")
    
    def book_room(self):
        if (len(self.guests) == 0) or (len(self.rooms) == 0):
            return print("\nRooms and/or guests not found!")
        g_id, r_id, d = 0, 0, 0
        pos_g, pos_r = 0, 0
        
        while True:
            try:
                g_id = abs(int(input("\nGuest ID: ")))
                flag = False
                
                for i, g in enumerate(self.guests):
                    if g_id == g.id:
                        flag, pos_g = True, i
                
                if flag:
                    break
                print(f"\nGuest ID {g_id} not found.")
            except ValueError:
                continue
        
        while True:
            try:
                r_id = abs(int(input("\nRoom ID: ")))
                flag = False
                
                for i, r in enumerate(self.rooms):
                    if r_id == r.id:
                        flag, pos_r = True, i
                
                if flag:
                    break
                print(f"\nRoom ID {r_id} not found.")
            except ValueError:
                continue
        
        while d == 0:
            try:
                d = abs(int(input("\nDays: ")))
            except ValueError:
                continue
        
        g, r = self.guests[pos_g], self.rooms[pos_r]
        if g.booked_room is None and r.available:
            r.book()
            g.book_room(r)
            print(f"\nBooking was successful. Total cost: {r.calculate_cost(d)}")
        else:
            print(f"\nEither the Guest {g_id} is already booked or Room {r_id} isn't available!")
    
    def checkout_guest(self):
        if len(self.guests) == 0:
            return print("\nNo guests found!")
        id, pos = 0, 0
        
        while True:
            try:
                id = abs(int(input("\nGuest ID: ")))
                flag = False
                
                for i, g in enumerate(self.guests):
                    if id == g.id:
                        flag, pos = True, i
                
                if flag:
                    break
                print(f"\nGuest ID {id} not found!")
            except ValueError:
                continue
        
        g = self.guests[pos]
        if g.booked_room is not None:
            g.booked_room.checkout()
            g.checkout()
            print("\nCheckout was successful!")
        else:
            print(f"\nGuest {id} hasn't booked a room!")
    
    def show_statistics(self):
        if (len(self.guests) == 0) or (len(self.rooms) == 0):
            return print("\nRooms and/or guests not found!")
        total_r, av_r, oc_r, total_g, max_exp_r, sum_dr = len(self.rooms), 0, 0, len(self.guests), 0, 0
        
        for r in self.rooms:
            dr = r.daily_rate
            sum_dr += dr
            if r.available:
                av_r += 1
            else:
                oc_r += 1
            if dr > max_exp_r:
                max_exp_r = dr
        
        print(f"\nTotal rooms: {total_r}\nAvailable: {av_r}\nOccupied: {oc_r}\nTotal guests: {total_g}\nMost expensive room: {max_exp_r}\nAverage daily room rate: {(sum_dr/total_r):.2f}")
        
def main():
    print("===== HOTEL MANAGEMENT SYSTEM =====")
    hotel = Hotel()
    
    while True:
        num = get_int("\n1. Show rooms\n2. Add room\n3. Show available rooms\n4. Find room\n5. Show guests\n6. Add guest\n7. Find guest\n8. Book room\n9. Checkout guest\n10. Show statistics\n11. Exit\n\nChoose: ")
        match(num):
            case 1: hotel.show_rooms()
            case 2: hotel.add_room()
            case 3: hotel.show_available_rooms()
            case 4: hotel.find_room()
            case 5: hotel.show_guests()
            case 6: hotel.add_guest()
            case 7: hotel.find_guest()
            case 8: hotel.book_room()
            case 9: hotel.checkout_guest()
            case 10: hotel.show_statistics()
            case 11: break
    
    print("\nGoodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
            return n if (1 <= n <= 11) else print("\nChoose between 1 and 11.")
        except ValueError:
            continue

main()

import re

PATTERN_NAME = r"[A-Za-z]+"

def main():
    print("===== SUPPORT TICKET ANALYZER =====")
    number = 0
    tickets = [
        {
            "id": "Ticket 1",
            "title": "Printer not working",
            "priority": "High",
            "status": "Open"
        },
        {
            "id": "Ticket 2",
            "title": "Password reset",
            "priority": "Low",
            "status": "Closed"
        },
        {
            "id": "Ticket 3",
            "title": "Network connection problem",
            "priority": "Critical",
            "status": "Open"
        }
    ]
    
    while number != 7:
        number = get_int("\n1. Show all tickets\n2. Show open tickets\n3. Show high priority tickets\n4. Count tickets by status\n5. Count tickets by priority\n6. Search ticket\n7. Exit\n\nChoose: ")
        match(number):
            case 1: show_tickets(tickets)
            case 2: show_open_tickets(tickets)
            case 3: show_high_critical_tickets(tickets)
            case 4: count_tickets_status(tickets)
            case 5: count_tickets_priority(tickets)
            case 6: search_ticket(tickets)
    
    print("Goodbye!")

def get_int(pr):
    while True:
        try:
            n = int(input(pr))
            if n not in [1,2,3,4,5,6,7]:
                print("Choose between 1 and 7")
                continue
        except ValueError:
            continue
        break
    
    return n

def show_tickets(t):
    for i in range(len(t)):
        print(f"{t[i]['id']} | {t[i]['title']} | {t[i]['priority']} | {t[i]['status']}")

def show_open_tickets(t):
    for i in range(len(t)):
        if t[i]["status"] == "Open":
            print(f"{t[i]['id']} | {t[i]['title']} | {t[i]['priority']} | {t[i]['status']}")

def show_high_critical_tickets(t):
    for i in range(len(t)):
        if t[i]["priority"] in ["High", "Critical"]:
            print(f"{t[i]['id']} | {t[i]['title']} | {t[i]['priority']} | {t[i]['status']}")

def count_tickets_status(t):
    o, ip, c = 0, 0, 0
    
    for i in range(len(t)):
        match(t[i]["status"]):
            case "Open": o += 1
            case "In Progress": ip += 1
            case "Closed": c += 1
    
    print(f"Open: {o}\nIn Progress: {ip}\nClosed: {c}")

def count_tickets_priority(t):
    h, c, low = 0, 0, 0
    
    for i in range(len(t)):
        match(t[i]["priority"]):
            case "High": h += 1
            case "Critical": c += 1
            case "Low": low += 1
    
    print(f"High: {h}\nLow: {low}\nCritical: {c}")

def search_ticket(t):
    s = ""
    
    while not re.fullmatch(PATTERN_NAME, s):
        s = input("Search: ")
    
    for i in range(len(t)):
        if s.lower() in t[i]["title"].lower():
            print(f"{t[i]['id']} | {t[i]['title']} | {t[i]['priority']} | {t[i]['status']}")

main()

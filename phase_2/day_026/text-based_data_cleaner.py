# Day 26 28/9/26

import re

PATTERN_STR = r"[A-Za-z0-9]+"
PATTERN_NUM = r"[0-9]+"

def main():
    print("===== DATA CLEANER =====")
    option = 0
    data = ["Kostas, 25, IT Support", "maria , 30 , HR", "GEORGE,27, Software Engineer",
    "nikos, , Sales", "anna,twenty,Marketing"]
    clean = []
    
    while True:
        option = get_number("\n1. Load raw data\n2. Show cleaned data\n3. Show invalid records\n4. Remove duplications\n5. Search records\n6. Show statistics\n7. Exit\n\nChoose: ")
        match(option):
            case 1: clean = load_raw_data(data)
            case 2: show_cleaned_data(clean)
            case 3: invalid = show_invalid_records(clean, data)
            case 4: removed = remove_duplicates(clean, data)
            case 5: search_records(clean, data)
            case 6: show_statistics(clean, invalid, removed)
            case 7: break
    
    print("\nGoodbye!")


def get_number(p):
    while True:
        try:
            n = int(input(p))
            if n not in [1,2,3,4,5,6,7]:
                continue
            break
        except ValueError:
            continue
        
    return n

def load_raw_data(d):
    new_d = []
    
    for s in d:
        s = s.replace(",", "|")
        w = s.split("|")
        new_s = ""
        
        for i in range(len(w)):
            w[i] = w[i].strip()
            if i == 0:
                w[i] = w[i].capitalize()
            if w[i] == "":
                w[i] = w[i].replace("", "Empty")
            if i == (len(w) - 1):
                new_s += w[i]
            else:
                new_s += w[i] + " | "
        
        new_d.append(new_s)
        
    return new_d

def show_cleaned_data(c):
    if check_emptiness(c):
        print("\nLoad data first.\n")
        return 0
    
    print()
    
    for i in range(len(c)):
        print(c[i])

def show_invalid_records(c, d):
    if check_emptiness(c):
        print("\nLoad data first.\n")
        return 0
    temp, j = [], 0
    
    for s in c:
        w = s.split(" | ")
        
        for i in range(len(w)):
            if (w[i] == "Empty") or (i == 1 and (not re.fullmatch(PATTERN_NUM, w[i]))):
                temp.append(d[j])
        
        j += 1
    
    print()
    
    for i in range(len(temp)):
        print(temp[i])
    
    return temp

def remove_duplicates(c, d):
    if check_emptiness(c):
        print("\nLoad data first.\n")
        return 0
    temp, count = [], 0
    
    for s in d:
        if s not in temp:
            temp.append(s)
        else:
            temp.remove(s)
            count += 1
            print("\nDuplicates removed.")
    
    
    print(f"\nUnique records: {len(d)}")
    return count

def search_records(c, d):
    if check_emptiness(c):
        print("\nLoad data first.\n")
        return 0
    txt = ""
    
    while not re.fullmatch(PATTERN_STR, txt): txt = input("\nSearch: ")
    
    for i in range(len(c)):
        if txt.lower() in c[i].lower():
            print(c[i])

def show_statistics(c, i, r):
    if check_emptiness(c):
        print("\nLoad data first.\n")
        return 0
    print("\n===== STATISTICS =====\n")

    for j in range(len(c)):
        print(c[j])
        
    total = len(c)
    invalid = len(i)
    valid = total - invalid
    print(f"\nTotal records: {total}\nValid records: {valid}\nInvalid records: {invalid}\nDuplicate records removed: {r}")

def check_emptiness(c):
    return True if len(c) == 0 else False
 
main()

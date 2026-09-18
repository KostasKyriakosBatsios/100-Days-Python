def main():
    print("===== WORD FREQUENCY ANALYZER =====")
    option = 0
    words = {}
    
    while option != 5:
        option = get_option("\n1. Analyze text.\n2. Show word frequencies.\n3. Search word.\n4. Show most common word.\n5. Exit.\n\nChoose an option from above: ")
        match(option):
            case 1:
                words = analyze_text()
            case 2:
                frequencies(words)
            case 3:
                search_word(words)
            case 4:
                most_common_word(words)
    
    print("Goodbye.")

def get_option(prompt):
    while True:
        try:
            o = int(input(prompt))
            if o not in [1,2,3,4,5]:
                print("\nChoose between 1 and 5.\n")
                continue
        except ValueError:
            continue
        break
    
    return o

def analyze_text():
    while True:
        s = input("\nEnter text: \n")
        if s == "" or s == " ":
            print("\nCannot be left empty!\n")
            continue
        break
    
    t_dict = clean_text(s)
    return t_dict

def clean_text(s):
    new_s = s.split(" ")
    temp = {}

    for w in new_s:
        for c in w:
            if c in [".", ",", "?", ";", ":", "!"]:
                w = w.replace(c, "")
        w = w.lower()
        if w not in temp:
            temp[f"{w}"] = 1
        else:
            temp[f"{w}"] += 1
    
    return temp

def frequencies(w):
    if check_emptiness(w):
        return
    print("\nWord frequencies: ")

    for k, v in w.items():
        print(f"{k}: {v}")

def search_word(w):
    if check_emptiness(w):
        return
    
    while True:
        s = input("\nEnter word: \n")
        if s == "" or s == " ":
            print("\nCannot be left empty!\n")
            continue
        break
    
    flag = False
    
    for k in w.keys():
        if s.lower() == k:
            print(f"\n'{k}' appears {w[k]} time/-s.")
            flag = True
    
    if not flag:
        print(f"\nWord '{s}' not found.")

def most_common_word(w):
    if check_emptiness(w):
        return
    
    most_frequent_word, max = "", 0
    print("\nMost common words: ")
        
    for k, v in w.items():
        if v >= max:
            max = v
            most_frequent_word = k
            print(f"{most_frequent_word}: {max}")

def check_emptiness(w):
    if w == {}:
        print("\nNo text has been analyzed yet.\n")
        return True

    return False

main()

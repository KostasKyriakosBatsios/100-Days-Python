import random as rn
import string

UPPER_LIST = string.ascii_uppercase
LOWER_LIST = string.ascii_lowercase
NUMS_LIST = string.digits
SPECIAL_CHARS_LIST = string.punctuation

def main():
    print("=== Password Generator ===")
    length = get_int("\nEnter password length: ")
    upper, lower, numbers, special_chars = answers()
    password = generate_password(upper, lower, numbers, special_chars, length)
    print(password)

def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 4 or n > 50:
                print("\nLength must be between 4 and 50")
                continue
        except ValueError:
            continue
        break

    return n

def answers():
    print("\nInclude:\n")
  
    while True:
        ans1, ans2, ans3, ans4 = "", "", "", ""

        while ans1 not in ["y", "n"]: ans1 = input("Uppercase letters? (y/n): ").lower()

        while ans2 not in ["y", "n"]: ans2 = input("Lowercase letters? (y/n): ").lower()

        while ans3 not in ["y", "n"]: ans3 = input("Numbers? (y/n): ").lower()

        while ans4 not in ["y", "n"]: ans4 = input("Special characters? (y/n): ").lower()

        if ans1 == "n" and ans2 == "n" and ans3 == "n" and ans4 == "n":
          print("You must select at least one character type.")
          continue
        else:
          break

    return ans1, ans2, ans3, ans4

def generate_password(u, l, n, sc, pwdlen):
    pwd = ""
    options = [(u, "upper"), (l, "lower"), (n, "numbers"), (sc, "special chars")]
    temp_list = [label for value, label in options if value == "y"]
    length = len(temp_list)
    pick  = ""
    i = 0
  
    while i < pwdlen:
        match(length):
            case 1: pick = ''.join(rn.choices(temp_list, weights=[100]))
            case 2: pick = ''.join(rn.choices(temp_list, weights=[50, 50]))
            case 3: pick = ''.join(rn.choices(temp_list, weights=[33.3, 33.3, 33.3]))
            case 4: pick = ''.join(rn.choices(temp_list, weights=[25, 25, 25, 25]))
        match(pick):
          case "upper":
            temp = list(UPPER_LIST)
            rn.shuffle(temp)
            temp2 = ''.join(temp)
            pwd += rn.choice(temp2)
          case "lower":
            temp = list(LOWER_LIST)
            rn.shuffle(temp)
            temp2 = ''.join(temp)
            pwd += rn.choice(temp2)
          case "numbers":
            temp = list(NUMS_LIST)
            rn.shuffle(temp)
            temp2 = ''.join(temp)
            pwd += rn.choice(temp2)
          case "special chars":
            temp = list(SPECIAL_CHARS_LIST)
            rn.shuffle(temp)
            temp2 = ''.join(temp)
            pwd += rn.choice(temp2)
        i += 1

    # Check if the password meets the criteria
    if u == "y" and not any(c in UPPER_LIST for c in pwd):
        pwd += rn.choice(UPPER_LIST)
    if l == "y" and not any(c in LOWER_LIST for c in pwd):
        pwd += rn.choice(LOWER_LIST)
    if n == "y" and not any(c in NUMS_LIST for c in pwd):
        pwd += rn.choice(NUMS_LIST)
    if sc == "y" and not any(c in SPECIAL_CHARS_LIST for c in pwd):
        pwd += rn.choice(SPECIAL_CHARS_LIST)

    return pwd

main()
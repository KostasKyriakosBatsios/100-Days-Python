# Day 5 22/8/26!

from random import choice

# Initialize lists that are constant (final)
LETTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER_LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
NUMBERS = [0,1,2,3,4,5,6,7,8,9]
SYMBOLS = ["!","@","#","$","%","^","&","*"]

def main():
    print("=== Password Generator ===")
    while True:
        # Type in the length of the password
        length = get_int("\nLength: ")

        # Series of questions
        up, num, sym = "", "", ""
        while up not in ["y", "n"]: up = input("Include uppercase? ").lower()
        while num not in ["y", "n"]: num = input("Include numbers? ").lower()
        while sym not in ["y", "n"]: sym = input("Include symbols? ").lower()

        # Generate the password based on the info above
        generate_pass(length, up, num, sym)

        # Ask if the user wants to generate another password
        con = ""
        while con not in ["y", "n"]: con = input("Generate another? ").lower()
        if con == "n":
            break

    print("\nGoodbye!")


# Function that gets the length that the generated password will have
def get_int(prompt):
    while True:
        try:
            var = int(input(prompt))
            if var <= 0:
                print("\nThe value must be positive\n")
                continue
        except ValueError:
            continue
        break

    return var

# Function that generates the password
def generate_pass(var1, var2, var3, var4):
    # Initializing the new_pass variable
    new_pass = ""

    """
    Based on the answers to the questions about uppercase, numbers and symbols, we choose randomly which character 
    will insert to the new password. For context: l = letters, ul = uppercase letters, n = numbers, s = symbols
    """
    for _ in range(var1):
        # Initialize a helper list
        temp = []

        l = choice(LETTERS)
        if var2 == "y" and var3 == "y" and var4 == "y":
            ul, n, s = choice(UPPER_LETTERS), str(choice(NUMBERS)), choice(SYMBOLS)
            temp.extend([l, ul, n, s])
            new_pass += choice(temp)
        elif var2 == "y" and var3 == "y" and var4 == "n":
            ul, n = choice(UPPER_LETTERS), str(choice(NUMBERS))
            temp.extend([l, ul, n])
            new_pass += choice(temp)
        elif var2 == "y" and var3 == "n" and var4 == "y":
            ul, s = choice(UPPER_LETTERS), choice(SYMBOLS)
            temp.extend([l, ul, s])
            new_pass += choice(temp)
        elif var2 == "y" and var3 == "n" and var4 == "n":
            ul = choice(UPPER_LETTERS)
            temp.extend([l, ul])
            new_pass += choice(temp)
        elif var2 == "n" and var3 == "y" and var4 == "y":
            n, s = str(choice(NUMBERS)), choice(SYMBOLS)
            temp.extend([l, n, s])
            new_pass += choice(temp)
        elif var2 == "n" and var3 == "y" and var4 == "n":
            n = str(choice(NUMBERS))
            temp.extend([l, n])
            new_pass += choice(temp)
        elif var2 == "n" and var3 == "n" and var4 == "y":
            s = choice(SYMBOLS)
            temp.extend([l, s])
            new_pass += choice(temp)
        else:
            temp.extend(l)
            new_pass += choice(temp)

    print(f"\nGenerated password: {new_pass}\n")

main()
# Day 7 25/8/26!

def main():
    print("=== Palindrome Checker ===")
    
    while True:
        # Ask the user to enter a word or phrase
        user_input = get_word("\nEnter text: ")

        # Check if the input is a palindrome
        if is_palindrome(user_input):
            print(f'\n"{user_input}" is a palindrome! ✓\n')
        else:
            print(f'\n"{user_input}" is not a palindrome. ✗\n')

        # Ask the user if they want to check another word or phrase
        again = ""
        while again not in ['y', 'n']: again = input("Check another? (y/n): ").strip().lower()
        if again == 'n':
            print("\nGoodbye!")
            break

# Function to get user input
def get_word(prompt):
    while True:
        val = input(prompt)

        # Check if the input is empty (just pressed enter)
        if not val:
            print("No empty word/phrase.")
            continue

        # Check if the input includes only spaces
        if val.isspace():
            print("Input includes only spaces.")
            continue

        # Check if it includes improper characters (special characters and numbers)
        if not val.isalpha():
            print("Please enter only letters (no numbers or special characters).")
            continue

        break

    return val

# Function to check if a word or phrase is a palindrome
def is_palindrome(val):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_val = ''.join(val.split()).lower()

    # Check if the value is a palindrome by comparing it to its reverse
    return cleaned_val == cleaned_val[::-1]

main()
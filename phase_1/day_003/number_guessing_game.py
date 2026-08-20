# Day 3 20/8/26!

# Use library random to generate an integer between our desired range
from random import randint

def main():
    print("=== Number Guessing Game ===")
    while True:
        print("\nI'm thinking of a number between 1 and 100.\n")

        # Generate a random number between 1 and 100
        rnd_num = randint(1,101)

        # Variable that calls function guess and returns how many attempts the user took to guess the number
        attempt_count = guess(rnd_num)
        print(f"You found it in {attempt_count} attempts.")

        # Ask if the user wants to play the guessing game again
        con = ""
        while con not in ["y","n"]:
            con = input("Play again? (y/n): ").lower()
        if con == "n":
            print("\nThanks for playing!")
            break

# Function that the user guesses the number
def guess(num):
    # Variable that checks if the user guessed right, plus an attempt counter one
    flag = True
    count = 0
    
    # The user tries to guess the number
    while flag:
        try:
            guess = int(input("Enter your guess: "))
            if guess <= 0 or guess > 100:
                print("\nInvalid guess.")
                continue
        except ValueError:
            continue
    
        count += 1
    
        if guess > num:
            print("Too high!\n")
        elif guess < num:
            print("Too low!\n")
        else:
            print("Congratulations! You found it🎉!\n")
            flag = False

    return count

main()
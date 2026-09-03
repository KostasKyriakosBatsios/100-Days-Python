import random as rn
import re

PATTERN = r"[a-z]"
WORDS = ["python", "computer", "programming", "developer", "keyboard", "network", "database", "function", "variable", "algorithm"]

def main():
    print("=== HANGMAN ===\n")
    while True:
        print("I'm thinking of a word ...\n")
        chosen = rn.choice(WORDS)
        WORDS.remove(chosen)
        length = len(chosen)
        flag = guess_word(chosen, length, "Guess a letter: ")

        if flag:
            print("🎉 You won!\n")
        else:
            print(f"💀 Game Over!\n\nThe word was: {chosen}\n")

        answer = ""
        while answer not in ["y","n"]: answer = input("Play again? (y/n): ").lower()

        if answer == "n":
            print("Thanks for playing!")
            break
        

def guess_word(w, l, prompt):
    alphabet = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ', 'z ']

    attempts = 0
    found = []

    for i in range(l):
        found.append("_ ")

    print(f"Word: {''.join(found)}")

    while attempts < 10:

        while True:
            letter = input(prompt)
            formatted = letter + " "

            if (formatted in found) or (formatted not in alphabet):
                print("You already guessed that letter.")
                continue

            if re.fullmatch(PATTERN, letter):
                break
            else:
                print("\nNo numbers and special character!\n")

        if letter in w:
            print("Good guess! ✓\n")
            alphabet.remove(formatted)
            for i in range(l):
                if w[i] == letter:
                    found[i] = formatted

            print(f"Word: {''.join(found)}")

            if found.count("_ ") > 0:
                continue
            else:
                break
                
        else:
            attempts += 1
            print(f"Wrong! ✗\nAttempts remaining: {10 - attempts}\n")
            alphabet.remove(formatted)

    for i in range(len(found)):
        if found[i] == "_ ":
            return False
    
    return True     

main()
# Day 4 22/8/26!

from random import choice

CHOICES = ("Rock", "Paper", "Scissors")

def main():
    # Initialize the score
    score_user, score_computer, score_tie = 0, 0, 0
    print("=== Rock, Paper, Scissors ===\n")

    while True:
        # Ask what the user wants to choose, and then the computer chooses
        user_pick = get_choice("Choose your move:\n1. Rock\n2. Paper\n3. Sciccors\n\nYour choice: ")
        computer_pick = choice(["Rock", "Paper", "Scissors"])

        # Let's play!
        print(f"\nYou chose: {user_pick}")
        print(f"Computer chose: {computer_pick}\n")
        winner = get_game_winner(user_pick, computer_pick)

        # Update the score
        if winner == "player": score_user += 1
        elif winner == "computer": score_computer += 1
        else: score_tie += 1
        print(f"\nScore:\nPlayer: {score_user}\nComputer: {score_computer}\nTies: {score_tie}\n")

        # Ask if the user wants to play again!
        con = ""
        while con not in ["y", "n"]: con = input("Play again? (y/n): ")
        if con == "n":
            print(f"=== Final Score ===\nPlayer: {score_user}\nComputer: {score_computer}\nTies: {score_tie}\n")
            if score_user > score_computer:
                print("You are the winner! 🏆")
            elif score_computer > score_user:
                print("Computer is the winner!")
            else:
                print("It's a draw! 🤝")
            break

# Function that gets the answer from the user
def get_choice(prompt):
    while True:
        pick = input(prompt)
        if pick not in CHOICES:
            continue
        break

    return pick

# Function that returns the winner of the round
def get_game_winner(p1_choice, p2_choice):
    if p1_choice == "Rock":
        if p2_choice == "Rock":
            print("It's a tie!")
            return "tie"
        elif p2_choice == "Paper":
            print("Computer wins!")
            return "computer"
        else:
            print("You won! 🎉")
            return "player"
    elif p1_choice == "Paper":
        if p2_choice == "Rock":
            print("You won! 🎉")
            return "player"
        elif p2_choice == "Paper":
            print("It's a tie!")
            return "tie"
        else:
            print("Computer wins!")
            return "computer"
    else:
        if p2_choice == "Rock":
            print("Computer wins!")
            return "computer"
        elif p2_choice == "Paper":
            print("You won! 🎉")
            return "player"
        else:
            print("It's a tie!")
            return "tie"   

main()
# Day 9 27/8/26!

from operator import index
import random

def main():
    print("=== Python Quiz ===")
    
    while True:
        # Variable that stores the questions and answers
        q_and_a = [
            {"id": 1, "question": "Which keyword is used to define a function in Python?", "options": ["def", "class", "return", "print"], "answer": "def"},
            {"id": 2, "question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "16", "32"], "answer": "8"},
            {"id": 3, "question": "How do you create a list in Python?", "options": ["{}", "()", "<>", "[...]"], "answer": "[...]"},
            {"id": 4, "question": "What does the len() function do?", "options": ["Returns the length of an object", "Returns the type of an object", "Returns the value of an object", "Returns the keys of an object"], "answer": "Returns the length of an object"},
            {"id": 5, "question": "How do you access an element in a list?", "options": ["Using a key in curly brackets", "Using an index in square brackets", "Using a value in parentheses", "Using a label in angle brackets"], "answer": "Using an index in square brackets"}
        ]

        # Return how many answers were correct and wrong and total score
        correct, wrong, score = ask_question(q_and_a)

        # Print the results
        print("=== Quiz Complete ===")
        print(f"Correct answers: {correct}\nWrong answers: {wrong}\nTotal score: {score}%")

        # Ask the user if they want to play again
        again = ""
        while again not in ["y", "n"]: again = input("Play again? (y/n): ").lower()
        if again == "n":
            print("Thank you for playing!")
            break

# Function to ask the question and get the user's answer
def ask_question(var):
    count1, count2, total = 0, 0, 0
    length = len(var)
    q_num = 1
    while length > 0:
        # Randomly pick a question from the list
        q = random.choice(var)
        print(f"\nQuestion {q_num}/5\n\n{q['question']}")
        for number, option in enumerate(q['options'], start=1):
            print(f"{number}. {option}")

        # Get the user's answer and validate it
        try:
            a = int(input("\n\nYour answer: "))
            if a not in [1,2,3,4]:
                print("Please enter a valid option (1-4).")
                continue
        except ValueError:
            continue

        # Check if the answer is correct
        if q['options'][a-1] == q['answer']:
            print("Correct! ✓")
            count1 += 1
        else:
            print(f"Wrong! ✗\nYour answer: {a}. {q['options'][a-1]}\nCorrect answer: {q['options'].index(q['answer']) + 1}. {q['answer']}")
            count2 += 1

        # Remove the question from the list to avoid repetition
        var.remove(q)
        length = len(var)
        q_num += 1

    # Calculate the total score
    total = (count1 / 5) * 100

    return count1, count2, total

main()
# Day 1 18/8/26

HISTORY = []

def main():
    while True:
        # Ask if the user wants to see the history
        his = input("Wanna view the history of calculations? (y/n)").lower()
        if his == "y":
            for i in range(len(HISTORY)):
                print(HISTORY[i])

        # Ask the user for the 1st number, then the operator and then the 2nd number
        num1 = get_int("\nEnter 1st number: ")
        while True:
            op = input("Enter operation: ")
            if op not in ["+", "-", "*", "/", "**", "%"]:
                continue
            break
        num2 = get_int("Enter 2nd number: ")

        # Call function to make the operation between the numbers and return the result
        res = operations(num1,op,num2)
        if res == "":
            HISTORY.append(f"{num1} {op} {num2}")
        else:
            print(f"\nResult: {res}")
            HISTORY.append(f"{num1} {op} {num2} = {res}")

        # Ask the user, and depending on the answer, we'll continue or not
        con = input("\nDo you want to continue? (y/n): ").lower()
        if con == "n":
            print("\nGoodbye!")
            break

# Function to get the valid number the user gives
def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            continue
        break

    return number

def operations(first,operation,second):
    # Initialize total
    total = 0

    # Use match for every operation possible
    match(operation):
        case "+": total = first + second
        case "-": total = first - second
        case "*": total = first * second
        case "**":total = first ** second
        case "%": total = first % second
        case "/":
            try:
                total = first / second
            except ZeroDivisionError:
                print("You cannot divide when the 2nd number is 0!")
                return ""

    return total

main()
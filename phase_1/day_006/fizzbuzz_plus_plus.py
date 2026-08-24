# Day 6 24/8/26!

def main():
    print("=== FizzBuzz Generator ===\n")

    # Ask the user to give the start number and the end number
    start, end = get_numbers("Start: ", "End: ")
    print()
    
    # Apply the FizzBuzz rules
    fizz, buzz, fizzbuzz, num = FizzBuzz(start, end+1)

    # Display statistics
    print(f"\n=== Statistics ===\n")
    print(f"Fizz: {fizz}\nBuzz: {buzz}\nFizzBuzz: {fizzbuzz}\nNumbers: {num}")

# Function that gets the numbers properly
def get_numbers(prompt1, prompt2):
    # Ask for the 1st number
    while True:
        try:
            num1 = int(input(prompt1))
            if num1 <= 0:
                print("Only positive numbers!")
                continue
        except ValueError:
            continue
        break

    # Ask for the 2nd number
    while True:
        try:
            num2 = int(input(prompt2))
            if num2 <= 0:
                print("Only positive numbers!")
                continue
            if num2 < num1:
                print("2nd number must be bigger or at least equal to the 1st number!")
                continue
        except ValueError:
            continue
        break

    return num1, num2

# Function that checks which number is Fizz, Buzz, FizzBuzz or just a number
def FizzBuzz(num1, num2):

    # Initialize counters for fizz, buzz, fizzbuzz numbers and for plain numbers
    f, b, fb, n = 0, 0, 0, 0
    for i in range(num1,(num2)):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
            fb += 1
        elif i % 3 == 0:
            print("Fizz")
            f += 1
        elif i % 5 == 0:
            print("Buzz")
            b += 1
        else:
            print(i)
            n += 1

    return f, b, fb, n

main()
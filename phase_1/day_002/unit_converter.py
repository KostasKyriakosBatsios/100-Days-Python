# Day 2 19/8/26!

def main():
    while True:
        print("=== Unit Converter ===\n")

        # Ask the user which category wants to choose
        category = get_answer("1. Length\n2. Temperature\n3. Weight\n4. Volume\n5. Time\n\nChoose category: ")

        # Check based on the category, in order to make the proper conversions
        if category == 1:
            convert_length("\nChoose conversion: \n1. Kilometers → Miles\n2. Miles → Kilometers\n" \
            "3. Meters → Feet\n4. Feet → Meters\n\nChoose: ")
        elif category == 2:
            convert_temperature("Choose conversion: \n1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius\n\nChoose: ")
        elif category == 3:
            convert_weight("Choose conversion: \n1. kg → pounds\n2. pounds → kg\n\nChoose: ")
        elif category == 4:
            convert_volume("\nChoose conversion: \n1. Liters → Gallons\n2. Gallons → Liters\n" \
            "3. Milliliters → Fluid Ounces\n4. Fluid Ounces → Milliliters\n\nChoose: ")
        else:
            convert_time("\nChoose conversion: \n1. Seconds → Minutes\n2. Minutes → Seconds\n" \
            "3. Minutes → Hours\n4. Hours → Minutes\n5. Hours -> Days\n6. Days -> Hours\n\nChoose: ")

        # Ask if the user wants to continue
        continuing = ""
        while continuing not in ["y","n"]:
            continuing = input("Do you want to make another conversion? (y/n): ").lower()

        if continuing == "n":
            print("\nGoodbye!")
            break

# Function that gets the answer of which category the user wants to use
def get_answer(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a not in [1,2,3,4,5]:
                print("\nInvalid option\n")
                continue
        except ValueError:
            print()
            continue
        break

    return a

# Function that converts category length
def convert_length(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a not in [1,2,3,4]:
                print("\nInvalid option\n")
                continue
        except ValueError:
            print()
            continue
        break

    while True:
        try:
            val = float(input("\nEnter value: "))
        except ValueError:
            print()
            continue
        break

    if a == 1: print(f"\nResult: {(val*0.621371):.1f} miles\n")
    elif a == 2: print(f"\nResult: {(val/0.621371):.1f} kilometers\n")
    elif a == 3: print(f"\nResult: {(val*3.28084):.1f} feet\n")
    else: print(f"\nResult: {(val/3.28084):.1f} meters\n")

# Function that converts category temperature
def convert_temperature(prompt):
    while True:
            try:
                a = int(input(prompt))
                if a not in [1,2]:
                    print("\nInvalid option\n")
                    continue
            except ValueError:
                print()
                continue
            break
    
    while True:
        try:
            val = float(input("\nEnter value: "))
        except ValueError:
            print()
            continue
        break

    if a == 1: print(f"\nResult: {((val*1.8)+32):.1f} F°\n")
    else: print(f"\nResult: {((val-32)/1.8):.1f} C°\n")

# Function that converts category weight
def convert_weight(prompt):
    while True:
            try:
                a = int(input(prompt))
                if a not in [1,2]:
                    print("\nInvalid option\n")
                    continue
            except ValueError:
                print()
                continue
            break
    
    while True:
        try:
            val = float(input("\nEnter value: "))
        except ValueError:
            print()
            continue
        break

    if a == 1: print(f"\nResult: {(val*2.20462):.1f} pounds\n")
    else: print(f"\nResult: {(val/2.20462):.1f} kg\n")

# Function that converts category volume
def convert_volume(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a not in [1,2,3,4]:
                print("\nInvalid option\n")
                continue
        except ValueError:
            print()
            continue
        break

    while True:
        try:
            val = float(input("\nEnter value: "))
        except ValueError:
            print()
            continue
        break

    if a == 1: print(f"\nResult: {(val/3.785):.1f} gallons\n")
    elif a == 2: print(f"\nResult: {(val*3.785):.1f} liters\n")
    elif a == 3: print(f"\nResult: {(val*0.033814):.1f} oz\n")
    else: print(f"\nResult: {(val/0.033814):.1f} ml\n")

# Function that converts category time
def convert_time(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a not in [1,2,3,4,5,6]:
                print("\nInvalid option\n")
                continue
        except ValueError:
            print()
            continue
        break

    while True:
        try:
            val = float(input("\nEnter value: "))
        except ValueError:
            print()
            continue
        break

    if a == 1: print(f"\nResult: {(val/60):.1f} mins\n")
    elif a == 2: print(f"\nResult: {(val*60):.1f} sec\n")
    elif a == 3: print(f"\nResult: {(val//60)} hours and {(val%60)} mins\n")
    elif a == 4: print(f"\nResult: {(val*60):.1f} mins\n")
    elif a == 5: print(f"\nResult: {(val//24):.1f} days and {(val%24)} hours\n")
    else: print(f"\nResult: {(val*24):.1f} hours\n")

main()
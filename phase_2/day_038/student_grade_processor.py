# Day 38 13/10/26

def main():
    print("====== STUDENT GRADE PROCESSOR ======")
    grades, temp = [], []
    
    while True:
        num = get_num("\n1. Enter grades\n2. Display all grades\n3. Display passing grades\n4. Display grades as percentages\n5. Display grades sorted ascending\n6. Display statistics\n7. Exit\n\nChoose: ")
        match(num):
            case 1:
                temp = add_grades()
                if len(temp) > 0:
                    for g in temp:
                        grades.append(g)
            case 2:
                if len(grades) > 0:
                    display_grades(grades)
                else:
                    print("\nNo grades found!")
            case 3:
                if len(grades) > 0:
                    passing_grades = list(filter(lambda x : x >= 5, grades))
                    if len(passing_grades) > 0:
                        display_grades(passing_grades)
                    else:
                        print("\nNo passing grades found!")
                else:
                    print("\nNo grades found!")
            case 4:
                if len(grades) > 0:
                    grades_percentages = list(map(lambda x : x * 10, grades))
                    display_grades_percentages(grades_percentages)
                else:
                    print("\nNo grades found!")
            case 5:
                if len(grades) > 0:
                    grades_sorted = sorted(grades)
                    display_grades(grades_sorted)
                else:
                    print("\nNo grades found!")
            case 6:
                if len(grades) > 0:
                    show_statistics(grades)
                else:
                    print("\nNo grades found!")
            case 7:
                break

    print("\nGoodbye!")

def get_num(p):
    while True:
        try:
            n = int(input(p))
            if 1 <= n <= 7:
                return n
            print("\nNumber must be positive and between 1 and 7.")
        except ValueError:
            print("\nOnly numbers are acceptable!")
            continue

def add_grades():
    ans, temp = "", []
    
    while True:
        ans = input("\nEnter grade (0-10) or 'done' to finish: ")
        if ans.lower() == "done":
            break
        try:
            ans = float(ans)
        except ValueError:
            continue
        if 0 <= ans <= 10:
            temp.append(ans)
        else:
            print("\nGrade cannot be outside of 0-10 range.")
        
    if len(temp) > 0:
        print(f"\n{len(temp)} grades added successfully!")
    else:
        print("\nNo grades added!")
    return temp

def display_grades(g):
    for i in range(len(g)):
        print(f"Grade {i+1}: {g[i]}")

def display_grades_percentages(g):
    for i in range(len(g)):
        print(f"Grade {i+1}: {(g[i]):.1f}%")

def show_statistics(arr1):
    total, length, max_g, min_g, suc_g, fail_g = 0, len(arr1), 0, 10, 0, 0
    
    for g in arr1:
        total += g
        if g >= max_g:
            max_g = g
        if g <= min_g:
            min_g = g
        if g >= 5:
            suc_g += 1
        else:
            fail_g += 1
    
    print(f"\nTotal grades: {length}\nAverage: {(total/length):.2f}\nHighest grade: {max_g}\nLowest grade: {min_g}\nSuccessful grades: {suc_g}\nFailed grades: {fail_g}")

main()

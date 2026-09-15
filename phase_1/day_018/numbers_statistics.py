# Day 18 15/9/26!

def main():
    print("=== Number Statistics ===\n")
    num_list = get_numbers("\nEnter numbers separated by spaces: ")
    pop = len(num_list)
    total = sum(num_list)
    avg = total / pop
    smallest = min(num_list)
    biggest = max(num_list)
    num_list_sorted = sorted(num_list)
    print(f"\n=== Statistics ===\n\nNumbers: {pop}\nSum: {total}\nAverage: {avg:.2f}\nMinimum: {smallest}\nMaximum: {biggest}\n\nSorted: {num_list_sorted}")
  

def get_numbers(prompt):
    n = []
  
    while len(n) == 0: n = input(prompt).split(" ")

    n = ' '.join(n).split()
  
    for i in range(len(n)):
      try:
        n[i] = int(n[i]) if n[i].isdigit() else float(n[i])
      except ValueError:
        
        while True:
          try:
            temp = input(f"Re-enter a number at position {i + 1}: ")
            n[i] = int(temp) if temp.isdigit() else float(temp)
          except ValueError:
              continue
          break

    return n

main()
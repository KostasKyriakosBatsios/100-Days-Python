# Day 27 29/9/26

def main():
    print("===== BANK ACCOUNT =====")
    number = 0
    initial, current = 1000, 1000
    history = []
    
    while True:
        number = get_int("\n1. Show balance\n2. Deposit money\n3. Withdraw money\n4. Transaction history\n5. Account statistics\n6. Exit\n\nChoose: ")
        match(number):
            case 1: print(f"\nInitial balance: €{initial}\nCurrent balance: €{current:.2f}")
            case 2: current = deposit(current, history)
            case 3: current = withdraw(current, history)
            case 4: transactions(history)
            case 5: statistics(current, history)
            case 6: break
    
    print("Goodbye!")


def get_int(p):
    while True:
        try:
            n = int(input(p))
            if n not in [1,2,3,4,5,6]:
                continue
            break
        except ValueError:
            continue
    
    return n

def deposit(c, h):
    temp = {}
    
    while True:
        try:
            d = int(input("\nEnter amount to deposit: "))
            if d > 0:
                break
        except ValueError:
            continue
    
    temp["type"], temp["amount"] = "Deposit", d
    h.append(temp)
    c += d
    print(f"\nDeposit successful.\nCurrent balance: €{c}")
    return c

def withdraw(c, h):
    temp = {}
    
    while True:
        try:
            w = int(input("\nEnter amount to withdraw: "))
            if w > 0 and w <= c:
                break
            print("\nInsufficient funds.")
        except ValueError:
            continue
    
    temp["type"], temp["amount"] = "Withdraw", -w
    h.append(temp)
    c -= w
    print(f"\nWithdrawal successful.\nCurrent balance: €{c}")
    return c

def transactions(h):
    if len(h) == 0:
        print("\nNo history!")
        return 0
    
    i = 0
    print("\n===== TRANSACTION HISTORY =====\n")
    
    for i in range(len(h)):
        print(f"{i+1} {h[i]["type"]} {h[i]["amount"]}€")

def statistics(c, h):
    print("\n===== ACCOUNT STATISTICS =====\n")
    
    sum_d, sum_w, count_d, count_w, total_t = 0, 0, 0, 0, 0
    
    for i in range(len(h)):
        total_t += 1
        match(h[i]["type"]):
            case "Deposit":
                sum_d += h[i]["amount"]
                count_d += 1
            case "Withdraw":
                sum_w += abs(h[i]["amount"])
                count_w += 1
    
    print(f"Current balance: €{c:.2f}\n\nTotal deposits: €{sum_d:.2f}\nTotal withdrawals: €{sum_w:.2f}\n\nNumber of deposits: {count_d}\nNumber of withdrawals: {count_w}\nTotal transactions: {total_t}")

main()

# Day 41 16/10/26

import json
import requests


def main():
    print("========== POSTS MANAGER ==========")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
        response.raise_for_status()
    except requests.HTTPError:
        print("\nCouldn't complete properly the request!")
        return
    except requests.ConnectionError:
        print("\nConnection Failed!")
        return
    except requests.Timeout:
        print("\nThere was a timeout!")
        return

    while True:
        num = get_num(
            "\n1. Display all posts\n2. Search post by ID\n3. Display post by user ID\n4. Exit\n\nChoose: "
        )
        match (num):
            case 1:
                print(json.dumps(response.json(), indent=2))
            case 2:
                display_by_id(1)
            case 3:
                display_by_id(2)
            case 4:
                break

    print("\nGoodbye!")


def get_num(p):
    while True:
        try:
            n = int(input(p))
            if 1 <= n <= 4:
                return n
            print("\nChoose between 1 and 4!")
        except ValueError:
            print("\nOnly numbers!")
            continue


def display_by_id(ch):
    var = 0
    if ch == 1:
        pr = "\nPost ID: "
    else:
        pr = "\nUser ID: "

    while True:
        try:
            var = int(input(pr))
            if var > 0:
                break
            print("\nMust be a positive number!")
        except ValueError:
            print("\nOnly numbers!")
            continue
    
    if ch == 1:
        try:
            resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{var}", timeout=5)
            resp.raise_for_status()
        except requests.HTTPError:
            print("\nCouldn't complete properly the request!")
            return
        except requests.ConnectionError:
            print("\nConnection Failed!")
            return
        except requests.Timeout:
            print("\nThere was a timeout!")
            return
        print(json.dumps(resp.json(), indent=2))
    else:
        try:
            resp = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={var}", timeout=5)
            resp.raise_for_status()
        except requests.HTTPError:
            print("\nCouldn't complete properly the request!")
            return
        except requests.ConnectionError:
            print("\nConnection Failed!")
            return
        except requests.Timeout:
            print("\nThere was a timeout!")
            return
        p = resp.json()
        if p != []:
            print(json.dumps(p, indent=2))
        else:
            print(f"\nUser with ID {var} not found!")


main()

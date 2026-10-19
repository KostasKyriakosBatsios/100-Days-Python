# Day 42 19/10/26

import json
import re
import requests

URL = "https://jsonplaceholder.typicode.com/posts"
PATTERN_TITLE = r"[A-Za-z\s]+"


def main():
    print("===== POST EXPLORER =====")

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
        return

    match (response.status_code):
        case 200:
            posts = response.json()
        case _:
            print(f"\nError: {response.status_code}")
            return

    while True:
        number = get_int("\n1. Search post by ID\n2. Search posts by user ID\n3. Search posts by title keyword\n4. Display posts statistics\n5. Exit\n\nChoose between 1 and 5: ")
        match (number):
            case 1:
                search_id(posts)
            case 2:
                search_userId(posts)
            case 3:
                search_title(posts)
            case 4:
                show_stats(posts)
            case 5:
                break

    print("\nGoodbye!")


def get_int(p):
    while True:
        try:
            n = int(input(p))
            if 1 <= n <= 5:
                return n
            print("\nAs said, choose a number between 1 and 5")
        except ValueError:
            print("\nOnly integers are acceptable!")
            continue


def search_id(ps):
    p_id = 0

    while True:
        try:
            p_id = int(input("\nPost ID: "))
            if p_id > 0:
                break
            print("\nNumber must be positive!")
        except ValueError:
            print("\nOnly integers are acceptable!")
            continue

    try:
        rsp = requests.get(URL + f"/{p_id}", timeout=5)
        rsp.raise_for_status()
    except requests.RequestException as e:
        print(e)
        return

    match (rsp.status_code):
        case 200:
            print(json.dumps(rsp.json(), indent=4))
        case _:
            print(f"\nError: {rsp.status_code}")


def search_userId(ps):
    u_id = 0

    while True:
        try:
            u_id = int(input("\nUser ID: "))
            if u_id > 0:
                break
            print("\nNumber must be positive!")
        except ValueError:
            print(f"\nOnly integers are acceptable!")
            continue

    try:
        rsp = requests.get(URL + f"?userId={u_id}", timeout=5)
        rsp.raise_for_status()
    except requests.RequestException as e:
        print(e)
        return

    match (rsp.status_code):
        case 200:
            us = rsp.json()
            if len(us) == 0:
                return print(f"\nUser with id {u_id} not found!")

            for u in us:
                print(f"\n{json.dumps(u, indent=4)}")

        case _:
            print(f"\nError: {rsp.status_code}")


def search_title(ps):
    t, flag = "", False

    while not re.fullmatch(PATTERN_TITLE, t):
        t = input("\nTitle: ")

    for p in ps:
        if t.lower() in p["title"].lower():
            flag = True
            print(f"\n{json.dumps(p, indent=4)}")

    if not flag:
        print(f"\nTitle {t} not found.")


def show_stats(ps):
    total_p, max_u, max_p = 0, 0, 0
    temp_l, temp_d = [], {}

    for p in ps:
        total_p += 1
        var = p["userId"]
        if var not in temp_l:
            temp_l.append(var)
            temp_d[var] = 1
        else:
            temp_d[var] += 1

    for k in temp_d.keys():
        if temp_d[k] >= max_p:
            max_p = temp_d[k]
            max_u = k

    print(f"\nTotal posts: {total_p}\nTotal users: {len(temp_l)}\nUser with most post:\n\tID: {max_u}\n\tPosts: {max_p}")


main()

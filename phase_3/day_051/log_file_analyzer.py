# Day 51 28/10/26

from pathlib import Path

# Resolves to the absolute directory containing the script
SCRIPT_DIR = Path(__file__).resolve().parent

class LogAnalyzer:
    def __init__(self, path):
        self.path = path


    def read_log(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return print("\nCannot find the file with that path!")

        for l in lines:
            print(l.rstrip())


    def count_levels(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return print("\nCannot find the file with that path!")

        counter = {}
        count_invalid = 0

        for l in lines:
            if l.strip():
                temp = l.split(maxsplit=3)
                if len(temp) == 4:
                    if temp[2] == "INFO":
                        if "INFO" not in counter.keys():
                            counter["INFO"] = 1
                        else:
                            counter["INFO"] += 1
                    elif temp[2] == "WARNING":
                        if "WARNING" not in counter.keys():
                            counter["WARNING"] = 1
                        else:
                            counter["WARNING"] += 1
                    elif temp[2] == "ERROR":
                        if "ERROR" not in counter.keys():
                            counter["ERROR"] = 1
                        else:
                            counter["ERROR"] += 1
                    else:
                        count_invalid += 1
                else:
                    count_invalid += 1

        for k, v in counter.items():
            print(f"{k}: {v}")

        print(f"\nTotal invalid messages: {count_invalid}")


    def find_errors(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return print("\nCannot find the file with that path!")

        for l in lines:
            if l.strip():
                temp = l.split(maxsplit=3)
                if len(temp) == 4:
                    if temp[2] == "ERROR":
                        print(l.rstrip())


    def count_messages(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return print("\nCannot find the file with that path!")

        count_unique = {}

        for l in lines:
            if l.strip():
                temp = l.split(maxsplit=3)
                if len(temp) == 4:
                    if temp[2] == "INFO":
                        l = str(temp[3]).rstrip()
                    elif temp[2] == "WARNING":
                        l = str(temp[3]).rstrip()
                    elif temp[2] == "ERROR":
                        l = str(temp[3]).rstrip()
                    else:
                        continue

                    if l not in count_unique.keys():
                        count_unique[f"{l}"] = 1
                    else:
                        count_unique[f"{l}"] += 1

        for k, v in count_unique.items():
            print(f"{k}: {v}")


    def display_summary(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return print("\nCannot find the file with that path!")

        count_v, count_i, count_info, count_warning, count_error = 0, 0, 0, 0, 0
        count_unique = {}
        
        for l in lines:
            if l.strip():
                temp = l.split(maxsplit=3)
                if len(temp) == 4:
                    if temp[2] in ["INFO", "WARNING", "ERROR"]:
                        count_v += 1

                        if temp[2] == "INFO":
                            count_info += 1
                            l = str(temp[3]).rstrip()
                        elif temp[2] == "WARNING":
                            count_warning += 1
                            l = str(temp[3]).rstrip()
                        elif temp[2] == "ERROR":
                            count_error += 1
                            l = str(temp[3]).rstrip()

                        if l not in count_unique.keys():
                            count_unique[f"{l}"] = 1
                        else:
                            count_unique[f"{l}"] += 1
                    else:
                        count_i += 1
                else:
                    count_i += 1

        print(f"\nTotal valid logs: {count_v}\n\nINFO: {count_info}\nWARNING: {count_warning}\nERROR: {count_error}\n\nInvalid logs: {count_i}\n\nMost frequent messages:")

        # item[0] = key, item[1] = value
        for k, v in sorted(count_unique.items(), key=lambda item: item[1], reverse=True):
            print(f"{k}: {v}")


def main():
    print("========== LOG ANALYZER ==========")

    la_obj = LogAnalyzer(SCRIPT_DIR / "app.log")

    while True:
        num = get_num("\n1. Display all logs\n2. Count log levels\n3. Display errors\n4. Count repeated messages\n5. Display summary\n6. Exit\n\nChoose: ")

        match(num):
            case 1:
                la_obj.read_log()
            case 2:
                la_obj.count_levels()
            case 3:
                la_obj.find_errors()
            case 4:
                la_obj.count_messages()
            case 5:
                la_obj.display_summary()
            case 6:
                break

    print("\nGoodbye!")


def get_num(p):
    while True:
        try:
            n = int(input(p))

            if 1 <= n <= 6:
                return n

            print("\nOnly integers between 1 and 6")
        except ValueError:
            print("\nOnly numbers!")


main()

import re
import csv
import os
from tabulate import tabulate

while True:
    name = input("Name: ").strip()
    email = input("Email: ").strip()

    format = r"^[\w.-]+\@[\w.-]+\.\w+$"
    is_valid = re.search(format, email)

    if is_valid:
        file_exists = os.path.exists("contacts_log.csv")

        with open("contacts_log.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email"])

            if not file_exists:
                writer.writeheader()
            writer.writerow({"name": name, "email": email})
        break
    else:
        print("Invalid email format. Please use: username@domain.extension")

with open("contacts_log.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

    print(f"\nTotal contacts logged: {len(rows)}")

view = input("View total contacts logged? (y/n): ").strip().lower()
if view == "y":
    if rows:
        print(tabulate(rows, headers="keys", tablefmt="grid"))
    else:
        print("Nothing in file yet")
elif view == "n":
    print("Goodbye")
else:
    print("Please enter y or n")
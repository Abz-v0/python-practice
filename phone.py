import re

phone = input("Your phone number: ")

if is_valid := re.search(r"^0\d{10}$", phone):
    print("Valid")
else:
    print("Invalid")
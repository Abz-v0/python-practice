import re
import sys

users = {
    "abz": "python123",
    "tobi": "secure456",
    "chidi": "hackme789",
    "kemi": "django2024"
}

MAX_ATTEMPTS = 3
attempts = 0

USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
PASSWORD_PATTERN = re.compile(r"^(?=.*\d).{8,}$")

while attempts < MAX_ATTEMPTS:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not USERNAME_PATTERN.match(username):
        print("Invalid username format.\n")
        continue

    if not PASSWORD_PATTERN.match(password):
        print("Invalid password format.\n")
        continue

    if username in users and users[username] == password:
        print(f"\nWelcome, {username}!")
        sys.exit(0)

    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    print("\nInvalid username or password.")

    if remaining > 0:
        print(f"Attempts remaining: {remaining}\n")
    else:
        print("Too many failed attempts. Locked out.")
        sys.exit(1)
import random
import string

length = int(input("Password length: "))
password = ""
chars = string.ascii_letters + string.digits

for _ in range(length):
    password += random.choice(chars)

print(f"Your Password: {password}")
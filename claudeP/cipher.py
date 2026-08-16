import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python cipher.py key")

try:
    key = int(sys.argv[1])
except ValueError:
    sys.exit("Argument must be a digit")

cipher_text = ""
text = input("Text: ")

for char in text:
    if char.isalpha():
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')

        shifted = ((ord(char) - base) + key ) % 26 + base

        cipher_text += chr(shifted)
    else:
        cipher_text += char

print(f"Output: {cipher_text}")
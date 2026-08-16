def main():
    isbn = input("ISBN-10: ")
    if is_valid_isbn(isbn) and calculate_checksum(isbn):
        print("Valid")
    else:
        print("Invalid")

def is_valid_isbn(isbn):
    if len(isbn) != 10:
        return False
    if not isbn[:9].isdigit():
        return False
    if not (isbn[9].isdigit() or isbn[9].upper() == 'X'):
        return False

    return True

def calculate_checksum(isbn):
    total = 0
    for i in range(len(isbn)):
        char = isbn[i]
        if char == 'X':
            digit = 10
        else:
            digit = int(char)
        weight = 10 - i
        total += digit * weight

    return total % 11 == 0

if __name__ == '__main__':
    main()
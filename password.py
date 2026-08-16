def main():

# Ask the user for a password (a string)
    password = input("Password: ")

# Prints "Strong password" if all rules pass, or "Weak password" if any fail
    if is_strong(password):
        print("Strong password")
    else:
        print("Weak password")

# Check it against these rules using separate functions per rule:
def is_strong(p):
    return pass_length(p) and at_least_one_digit(p) and at_least_one_uppercase(p) and at_least_one_lowercase(p)


# At least 8 characters long
def pass_length(p):
    if len(p) >= 8:
        return True
    else:
        return False

# Contains at least one digit
def at_least_one_digit(p):
    for char in p:
        if char.isdigit():
            return True
    return False

# Contains at least one uppercase letter
def at_least_one_uppercase(p):
    for char in p:
            if char.isupper():
                return True
    return False

# Contains at least one lowercase letter
def at_least_one_lowercase(p):
    for char in p:
            if char.islower():
                return True
    return False

if __name__ == '__main__':
    main()
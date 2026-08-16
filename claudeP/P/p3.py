def main():
    while True:
        try:
            email = input("Email: ")
            if is_valid(email):
                print("Valid email")
                break
        except ValueError:
            pass

def is_valid(email):
    return contains_symbol(email) and at_least_one_char_before(email) and at_least_one_char_after(email)

def contains_symbol(email):
    if email.count("@") == 1:
        return True
    else:
        return False

def at_least_one_char_before(email):
    if email.index("@") > 0:
        return True
    else:
        return False

def at_least_one_char_after(email):
        if email.index("@") < len(email) - 1:
            return True
        else:
            return False

if __name__ == '__main__':
    main()
def main():
    # Get x safely, keep asking until valid
    x = get_number("What's x? ")

    # Get y safely, keep asking until valid AND not zero
    while True:
            y = get_number("What's y? ")
            try:
                result = x / y
            except ZeroDivisionError:
                print("Can't divide by zero")
            else:
                break

    print(result)

# Function to safely get a number (just checks it's a valid int)
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number")

if __name__ == '__main__':
    main()
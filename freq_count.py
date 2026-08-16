def main():
    # Ask the user to enter a sentence
    sentence = input("Enter a sentence: ").casefold()

    # Split it into words
    words = sentence.split()

    # Count how many times each word appears (using a dict)
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    print(count)


if __name__ == '__main__':
    main()
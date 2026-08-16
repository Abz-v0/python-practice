from collections import Counter

def main():
    word1 = input("First word: ").strip().casefold()
    word2 = input("Second word: ").strip().casefold()

    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")

    if Counter(word1) == Counter(word2):
        print("Anagrams")
    else:
        print("Not anagrams")


if __name__ == "__main__":
    main()
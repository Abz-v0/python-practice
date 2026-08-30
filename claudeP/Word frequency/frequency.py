import re
from collections import Counter

filename = input("File name: ").strip().lower()

try:
    if filename.endswith(".txt"):
        words = re.findall(r"\w+", open(filename).read(), re.IGNORECASE)
        cnt = Counter(words).most_common(3)
        print(cnt)
    else:
        print("Not a txt file")

except FileNotFoundError:
    print("File does not exist")
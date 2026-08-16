import sys

if len(sys.argv) != 2:
    print("Arguments must be 1")
    sys.exit(1)
    
# print((f"Hello, {sys.argv[1]}!\n") * len(sys.argv[1]), end="")
name = sys.argv[1]

for _ in range(len(name)):
    print(f"Hello, {name}!")
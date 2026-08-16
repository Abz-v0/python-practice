import sys
from python.psets.greetings import greet, farewell

if len(sys.argv) != 2:
    sys.exit("Too few arguments")

name = sys.argv[1]
print(f"{greet(name)}\n{farewell(name)}")
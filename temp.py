import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python temp.py [temperature] [unit]")

number = float(sys.argv[1])
unit = sys.argv[2].upper()

if unit == "C":
    result = (number * 9 / 5) + 32
    print(f"{result}°F")
elif unit == "F":
    result = (number - 32) * 5/9
    print(f"{result}°C")
else:
    sys.exit("Unit must be C or F")
import argparse

parser = argparse.ArgumentParser(description="type your name at the command line")
parser.add_argument("--name", default="World", type=str, help="a name to be typed")
name = parser.parse_args()

print(f"Hello, {name.name}!")
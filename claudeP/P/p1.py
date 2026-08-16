def main():
    name = input("Name: ")
    print(f"Initials: {initials(name)}")

def initials(name):
    words = name.split()
    initial_list = [word[0].upper() for word in words]
    final_initials = "".join(initial_list)
    return final_initials

main()
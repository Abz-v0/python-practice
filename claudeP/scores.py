choice = input("Add a new score, or view scores? (add/view): ")


if choice == "add":
    name = input("Name: ")
    score = input("Score: ")
    with open("scores.txt", "a") as file:
        file.write(f"{name},{score}\n")

elif choice == "view":
    with open("scores.txt", "r") as file:
        lines = file.readlines()
        if lines:
            print("--- All Scores ---")
            for line in sorted(lines):
                print(line.rstrip())
        else:
            print("Nothing in file yet")
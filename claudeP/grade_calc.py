def main():
    score = input("Score: ")
    score = int(score)
    grade = calculate_grade(score)
    print(f"Grade: {grade}")

def calculate_grade(score):
    if score > 100 or score < 0:
        return "Invalid input"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

main()
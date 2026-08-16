assignments = int(input("Assignments: "))
total_grade = 0

for assignment in range(assignments):
    # Score validation
    while True:
        try:
            score = int(input("Score: "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Weight validation
    while True:
        try:
            weight = float(input("Weight: "))
            if 0 <= weight <= 1:
                break
            else:
                print("Weight must be between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Math processing
    final_weighted_grade = score * weight
    total_grade += final_weighted_grade

# Convert the numeric grade to a letter grade
if total_grade >= 90:
    letter_grade = "A"
elif total_grade >= 80:
    letter_grade = "B"
elif total_grade >= 70:
    letter_grade = "C"
elif total_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Final output
print(f"Your final weighted grade is: {total_grade}")
print(f"Final Letter Grade: {letter_grade}")
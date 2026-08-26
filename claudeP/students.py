import csv

import statistics


students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)


scores = []
for student in students:
    scores.append(int(student["score"]))
    
average = statistics.mean(scores)

for student in students:
    name = student["name"]
    score = int(student["score"])
    if score >= average:
        print(f"{name}: {score} (Above average)")
    else:
        print(f"{name}: {score} (Below average)")

print(f"Average: {average}")
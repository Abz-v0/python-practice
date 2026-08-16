import random
import sys
import operator
import time

if len(sys.argv) != 2:
    sys.exit("Too few arguments")

num_questions = int(sys.argv[1])

q_num = 0
correct = 0

for _ in range(num_questions):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    symbols = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
    }

    chosen_symbol = random.choice(list(symbols.keys()))

    q_num += 1
    print(f"Question {q_num}: {num1} {chosen_symbol} {num2} = ?")

    start_question = time.time()
    user_answer = float(input("Your answer: "))
    end_question = time.time()

    time_for_this_question = end_question - start_question
    print(f"That toook you {time_for_this_question:.1f} seconds.")

    correct_answer = symbols[chosen_symbol](num1, num2)

    if user_answer == correct_answer:
        correct += 1
        print("Correct!")
    else:
        print(f"Incorrect! The answer was {correct_answer}")

print("The quiz is over!")
percentage = (correct / num_questions) * 100

print(f"You scored {percentage}%")

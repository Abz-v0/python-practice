import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

choice_emojis = { ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
choices = tuple(choice_emojis.keys())

def get_user_choice():
    while True:
      user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
      if user_choice in choices:
          return user_choice
      else:
          print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You chose: {choice_emojis.get(user_choice)}")
    print(f"Computer chose: {choice_emojis.get(computer_choice)}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win")
    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
  
        to_continue = input("Continue? (y/n): ").lower()
        if to_continue == "n":
            break
play_game()
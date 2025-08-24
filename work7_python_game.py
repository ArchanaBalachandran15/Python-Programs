# Rock Scissor and Paper Game in Python Using Random Module 

import random
images = {
    "rock": """
        ___
    ---'   __)
          (__)
          (__)
          ()
    ---.(__)
    """,
    "paper": """
         ___
    ---'    )____
              ____)
             ______)
            _______)
    ---.________)
    """,
    "scissors": """
         ___
    ---'    )____
              ____)
           __________)
          (__)
    ---.(__)
    """
}

print("Rules of the Rock-Paper-Scissors game are as follows: ")
print("Rock vs Paper -> win: Paper ")
print("Rock vs Scissors -> win: Rock ")
print("Paper vs Scissors -> win: Scissors ")

choices = ["rock", "paper", "scissors"]

while True:
    print("Choices are: ")
    print("0. Rock")
    print("1. Paper")
    print("2. Scissors")

    try:
        user_choice = int(input("Enter your choice in option number: (0-Rock, 1-Paper, 2-Scissors): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please enter 0, 1, or 2.")
        continue

    computer_choice = random.randint(0, 2)

    user_choice_name = choices[user_choice]
    computer_choice_name = choices[computer_choice]

    print("You chose: " + user_choice_name.capitalize())
    print(images[user_choice_name])

    print("Computer chose: " + computer_choice_name.capitalize())
    print(images[computer_choice_name])

    # logic
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != 'y':
        print("Hope you had fun! See you next time!!!")
        print("Thanks for playing!...")
        break

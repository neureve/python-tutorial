import random

options = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(options)
    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in options:
        print("Invalid choice. Try again.")
        continue

    if player == computer:
        print("It's a tie!")
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for playing!")
            break

    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win! Computer chose", computer)
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for playing!")
            break
    else:
        print("You lose! Computer chose", computer)
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for playing!")
            break

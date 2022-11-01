import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    araa = None

    while araa not in choices:
        araa = input("rock, paper, or scissors?: ").lower()

    if araa == computer:
        print("computer: ",computer)
        print("araa: ",araa)
        print("Tie!")

    elif araa == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("araa: ", araa)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("araa: ", araa)
            print("You win!")

    elif araa == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("araa: ", araa)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("araa: ", araa)
            print("You win!")

    elif araa == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("araa: ", araa)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("araa: ", araa)
            print("You win!")

    play_again = input("Wanna play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("See ya until next time")
import random

wins = 0
draws = 0
losses = 0
rounds = 0

keepPlaying = True
invalidInput = True

while keepPlaying:
    rounds += 1
    print("Welcome to Rock, Paper, Scissors!")

    invalidInput = True
    while invalidInput:
        player = input("\nEnter your choice: ")
        player = player.lower();

        invalidInput = False

        # Validate the player's choice
        if player == "rock":
            player = 1
        elif player == "paper":
            player = 2
        elif player == "scissors":
            player = 3
        else:
            print("Invalid option. Please try again.")
            invalidInput = True

    computer = random.randint(1, 3)

    print("\n")

    # Display the computer's choice
    if computer == 1:
        print("Computer chose Rock")
    elif computer == 2:
        print("Computer chose Paper")
    elif computer == 3:
        print("Computer chose Scissors")

    print("\n")

    # Inform if they won, lost, or tied with the opponent
    if player == computer:
        print("You tied!")
        draws += 1
    elif player == 1:
        if computer == 2:
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif player == 2:
        if computer == 1:
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif player == 3:
        if computer == 1:
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1

    print("\n")

    # By the end of each round, the player can choose whether to play again
    invalidInput = True
    while invalidInput:
        choice = input("Do you want to play again? (y/n): ")

        invalidInput = False

        if choice == "y":
            keepPlaying = True
        elif choice == "n":
            keepPlaying = False
        else:
            print("Invalid option. Please try again.")
            invalidInput = True

    print("\n")

# Display the final score
print("\nYou played " + str(rounds) + " rounds.")
print("Wins: " + str(wins))
print("Losses: " + str(losses))
print("Draws: " + str(draws))
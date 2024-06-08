# Importing a random module
import random

# Creating a list of play options
play = ["Rock", "Paper", "Scissors"]

# Assigning a random player to the system
computer = play[random.randint(0, 2)]

# Setting a player to False
player = False

# Seting a player to True
while player == False:

    player = input("Rock", "Paper", "scissors")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print ("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print ("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print ("You win!", player, "cuts", computer)
    else:
        print("That's not a valid play. Check the spelling!")

    # Player was set to true, but I want it to be false so the loop can continue
    player = False
    computer = play[random.randint(0, 2)]


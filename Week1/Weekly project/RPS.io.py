import random

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(rounds):
    player_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {player_choice}. Computer chose {computer_choice}.")
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score: You {player_score} - Computer {computer_score}")

        if (rounds == 3 and player_score >= 2) or (rounds == 5 and player_score >= 3):
            print("You have won the game!")
            return
        elif (rounds == 3 and computer_score >= 2) or (rounds == 5 and computer_score >= 3):
            print("The computer has won the game.")
            return

    if player_score > computer_score:
        print("You won the game!")
    elif player_score < computer_score:
        print("The computer won the game.")
    else:
        print("It's a tie game.")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    rounds = int(input("How many rounds do you want to play (3 or 5)? "))
    play_game(rounds)

if __name__ == "__main__":
    main()
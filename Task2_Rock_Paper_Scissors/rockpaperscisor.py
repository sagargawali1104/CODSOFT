import random
import time

def print_instructions():
    print("\n==============================")
    print(" Welcome to Rock-Paper-Scissors ")
    print("==============================")
    print("Rules:")
    print(" - Rock beats Scissors")
    print(" - Scissors beat Paper")
    print(" - Paper beats Rock")
    print("Type 'quit' anytime to exit.")
    print("==============================\n")

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        elif choice == "quit":
            return None
        else:
            print("Invalid input! Please type rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round(user_score, computer_score):
    user_choice = get_user_choice()
    if user_choice is None:
        return None, user_score, computer_score

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    time.sleep(0.5)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Current Score → You: {user_score} | Computer: {computer_score}\n")
    return True, user_score, computer_score

def play_game():
    print_instructions()
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        status, user_score, computer_score = play_round(user_score, computer_score)
        if status is None:
            break

        rounds_played += 1

        # Ask if user wants to continue
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\n==============================")
    print(" Final Results ")
    print("==============================")
    print(f"Rounds Played: {rounds_played}")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations, you are the overall winner!")
    elif computer_score > user_score:
        print("💻 Computer wins overall. Better luck next time!")
    else:
        print("🤝 It's an overall tie!")
    print("==============================")
    print("Thanks for playing Rock-Paper-Scissors!\n")

# Run the game
if __name__ == "__main__":
    play_game()

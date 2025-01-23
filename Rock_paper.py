import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    """Play the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        print("\nEnter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        try:
            # Prompt the user for their choice
            user_input = int(input("Your choice (1/2/3/4): "))
            if user_input == 4:
                print("\nThank you for playing! Final Scores:")
                print(f"User: {user_score}, Computer: {computer_score}")
                break
            
            choices = ["rock", "paper", "scissors"]
            if user_input not in [1, 2, 3]:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")
                continue

            user_choice = choices[user_input - 1]
            computer_choice = random.choice(choices)
            
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            # Determine the winner
            result = determine_winner(user_choice, computer_choice)
            if result == "tie":
                print("It's a tie!")
            elif result == "user":
                print("You win!")
                user_score += 1
            else:
                print("Computer wins!")
                computer_score += 1
            
            print(f"Scores -> You: {user_score}, Computer: {computer_score}")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    play_game()
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You won!"

    return "You lost!"

def main():
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

        if user_input == 'q':
            break

        if user_input not in options:
            print("Invalid input. Please try again.")
            continue

        computer_choice = random.choice(options)
        print("Computer picked", computer_choice)

        result = determine_winner(user_input, computer_choice)
        print(result)

        if result == "You won!":
            user_wins += 1
        elif result == "You lost!":
            computer_wins += 1

    print("You won", user_wins, "times")
    print("The computer won", computer_wins, "times")
    print("Goodbye!")

if __name__ == "__main__":
    main()


    
        
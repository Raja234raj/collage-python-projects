import random

def roll():
    return random.randint(1, 6)

def get_num_players():
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit() and 2 <= int(players) <= 4:
            return int(players)
        print("Invalid input. Must be between 2 - 4 players. Try again.")

def player_turn(player_idx, scores):
    print(f"\nPlayer number {player_idx + 1}'s turn has just started!")
    print(f"Your total score is: {scores[player_idx]}\n")
    
    current_score = 0
    while input("Would you like to roll (y)? ").lower() == "y":
        value = roll()
        print(f"You rolled a: {value}")

        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break

        current_score += value
        print(f"Your score is: {current_score}")

    scores[player_idx] += current_score
    print(f"Your total score is: {scores[player_idx]}")

def main():
    players = get_num_players()
    max_score = 50
    players_scores = [0] * players

    while max(players_scores) < max_score:
        for player_idx in range(players):
            player_turn(player_idx, players_scores)

    winning_idx = players_scores.index(max(players_scores))
    print(f"Player number {winning_idx + 1} is the winner with a score of: {max(players_scores)}")

if __name__ == "__main__":
    main()

    
    
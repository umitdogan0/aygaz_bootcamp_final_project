import random

# Global Skor Tablosu ve İstatistikler
total_games = 0
player_score = 0
computer_score = 0
total_moves = 0
most_chosen = {'rock': 0, 'paper': 0, 'scissors': 0}
player_points = 0

def show_statistics():
    print("\n--- Game Statistics ---")
    print(f"Total games played: {total_games}")
    print(f"Total player score: {player_score}")
    print(f"Total computer score: {computer_score}")
    print(f"Total moves made: {total_moves}")

    # En çok seçilen hamleyi bulma
    if total_moves == 0:
        most_chosen_move = 'unknown'
    else:
        most_chosen_move = max(most_chosen, key=most_chosen.get)
    
    print(f"Most chosen move: {most_chosen_move}")
    print(f"Total points: {player_points}")
    print("-----------------------\n")

def get_computer_choice(difficulty, player_choice=None):
    choices = ['rock', 'paper', 'scissors']
    if difficulty == 'easy':
        if random.random() < 0.1:
            return choices[(choices.index(player_choice) + 1) % 3]
        return random.choice(choices)
    elif difficulty == 'medium':
        if random.random() < 0.4:
            return choices[(choices.index(player_choice) + 1) % 3]
        return random.choice(choices)
    else:  # hard
        if player_choice and random.random() < 0.6:
            return choices[(choices.index(player_choice) + 1) % 3]
        return random.choice(choices)

def get_point_value(difficulty):
    if difficulty == 'easy':
        return 150
    elif difficulty == 'medium':
        return 300
    else:  # hard
        return 600

def play_game(difficulty, mode):
    global total_games, player_score, computer_score, total_moves, player_points
    
    if mode == 'quick':
        rounds_needed = 1
        score_multiplier = 0.5
        print("Mode Information: Single tour")
    elif mode == 'normal':
        rounds_needed = 2
        score_multiplier = 1
        print("Mode Information: 2 rounds win")
    elif mode == 'tournament':
        rounds_needed = 2
        score_multiplier = 1
        tournament_sets = 5
        print("Mode Information: 5 sets, 2 wins per set, winner of the tournament gets double points")
    else:
        print("Invalid game mode.")
        return
    
    if mode == 'tournament':
        player_set_wins = 0
        computer_set_wins = 0
        for set_number in range(1, tournament_sets + 1):
            print(f"\nSet {set_number} Start!")
            round_player_wins = 0
            round_computer_wins = 0
            set_point_value = get_point_value(difficulty)
            
            while round_player_wins < rounds_needed and round_computer_wins < rounds_needed:
                print("\nMake your move (rock, paper, scissors): ", end='')
                player_choice = input().lower()

                while player_choice not in choices:
                    player_choice = input("Invalid choice. Please choose (rock, paper, scissors): ").lower()

                # İstatistikleri Güncelleme
                total_moves += 1
                most_chosen[player_choice] += 1

                comp_choice = get_computer_choice(difficulty, player_choice)
                print(f"Computer's choice: {comp_choice}")

                if player_choice == comp_choice:
                    print("It's a tie!")
                elif (player_choice == 'rock' and comp_choice == 'scissors') or \
                     (player_choice == 'paper' and comp_choice == 'rock') or \
                     (player_choice == 'scissors' and comp_choice == 'paper'):
                    print("You win this round!")
                    round_player_wins += 1
                else:
                    print("You lose this round!")
                    round_computer_wins += 1

                print(f"Round score: You {round_player_wins} - {round_computer_wins} Computer")

            if round_player_wins == rounds_needed:
                print("You win this set!")
                player_set_wins += 1
                player_points += set_point_value
            else:
                print("Computer wins this set!")
                computer_set_wins += 1

        if player_set_wins > computer_set_wins:
            print("Congratulations! You win the tournament!")
            player_points *= 2  # Double points for tournament win
        else:
            print("Sorry, you lose the tournament!")
            computer_score += 1

    else:
        round_player_wins = 0
        round_computer_wins = 0
        point_value = get_point_value(difficulty)

        while round_player_wins < rounds_needed and round_computer_wins < rounds_needed:
            print("\nMake your move (rock, paper, scissors): ", end='')
            player_choice = input().lower()

            while player_choice not in choices:
                player_choice = input("Invalid choice. Please choose (rock, paper, scissors): ").lower()

            # İstatistikleri Güncelleme
            total_moves += 1
            most_chosen[player_choice] += 1

            comp_choice = get_computer_choice(difficulty, player_choice)
            print(f"Computer's choice: {comp_choice}")

            if player_choice == comp_choice:
                print("It's a tie!")
            elif (player_choice == 'rock' and comp_choice == 'scissors') or \
                 (player_choice == 'paper' and comp_choice == 'rock') or \
                 (player_choice == 'scissors' and comp_choice == 'paper'):
                print("You win this round!")
                round_player_wins += 1
            else:
                print("You lose this round!")
                round_computer_wins += 1

            print(f"Round score: You {round_player_wins} - {round_computer_wins} Computer")

        # Skor ve Puan Güncelleme
        if round_player_wins == rounds_needed:
            print("Congratulations! You win the game!")
            player_score += 1
            if mode == 'quick':
                player_points += point_value * 0.5
            elif mode == 'normal':
                player_points += point_value
        else:
            print("Sorry, you lose the game!")
            computer_score += 1

    total_games += 1

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play Game")
        print("2. Show Statistics")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            mode = input("Choose game mode (quick/normal/tournament): ").lower()
            while mode not in ['quick', 'normal', 'tournament']:
                mode = input("Invalid choice. Please choose game mode (quick/normal/tournament): ").lower()
            difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
            while difficulty not in ['easy', 'medium', 'hard']:
                difficulty = input("Invalid choice. Please choose difficulty level (easy/medium/hard): ").lower()
            play_game(difficulty, mode)
        elif choice == '2':
            show_statistics()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    choices = ['rock', 'paper', 'scissors']
    main_menu()

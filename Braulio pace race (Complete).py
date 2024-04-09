import random
import os

def display_race_track(snail_names, snails):
    print("\nRace Track:")
    for snail_name in snail_names:
        print(f"{snail_name}: {'-' * snails[snail_name]}>{' ' * (10 - snails[snail_name])}", end=" ")
    print()

def play_turn(snail_names, snails, order):
    for snail_name in order:
        print(f"\nIt's {snail_name}'s turn:")
        input("Press Enter to roll the dice...")

        try:
            rolled_snail = random.choice(snail_names)
            print(f"{snail_name} rolled {rolled_snail}")

            move_distance = random.randint(1, 3)
            snails[snail_name] += move_distance
            print(f"{snail_name} moves to space {snails[snail_name]}!")

            display_race_track(snail_names, snails)

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def save_game(snails):
    with open("race_progress.txt", "w") as file:
        for snail_name, position in snails.items():
            file.write(f"{snail_name}:{position}\n")

def load_game():
    if os.path.exists("race_progress.txt"):
        with open("race_progress.txt", "r") as file:
            snail_positions = {}
            for line in file:
                name, position = line.strip().split(":")
                snail_positions[name] = int(position)
        return snail_positions
    else:
        return None

print("Welcome to Braulio's Pace Race!")
print("Roll the dice and move your snail to reach the finish line first.")
print("Be careful not to roll someone else's color!")

snail_names = ['Michael', 'Jailen', 'Nicolas', 'Francis']

snails = load_game() or {name: 0 for name in snail_names}

order_of_snails = ['Michael', 'Jailen', 'Francis', 'Nicolas']

try:
    while all(position < 10 for position in snails.values()):
        play_turn(snail_names, snails, order_of_snails)
        save_game(snails)

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    winner_name = next(name for name, position in snails.items() if position >= 10)
    print(f"\n{winner_name} wins the race!")
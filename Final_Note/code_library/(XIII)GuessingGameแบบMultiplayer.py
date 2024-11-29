import random

def multiplayer_guessing_game():
    """เกมทายตัวเลขแบบเล่นหลายคน"""
    secret_number = random.randint(1, 100)
    max_attempts = 10
    players = int(input("Enter number of players: "))
    attempts = {player: 0 for player in range(1, players + 1)}

    print("\n***** Multiplayer Guessing Game *****")
    print(f"Secret number is between 1 and 100. Each player has {max_attempts} attempts.\n")

    for _ in range(max_attempts):
        for player in range(1, players + 1):
            guess = int(input(f"Player {player}, enter your guess: "))
            attempts[player] += 1

            if guess == secret_number:
                print(f"\nPlayer {player} wins! The secret number was {secret_number}.")
                return
            elif guess < secret_number:
                print(f"Player {player}, your guess is too low.")
            else:
                print(f"Player {player}, your guess is too high.")

    print(f"\nGame over! The secret number was {secret_number}.")
    for player, attempt in attempts.items():
        print(f"Player {player} made {attempt} attempts.")

multiplayer_guessing_game()

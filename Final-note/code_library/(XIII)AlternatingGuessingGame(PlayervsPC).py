import random

def alternating_guessing_game():
    """เกมที่ผู้เล่นและ PC สลับกันทาย ใครทายถูกก่อนชนะ"""
    secret_number = random.randint(1, 100)
    attempts = 10

    print("\n***** Alternating Guessing Game (Player vs PC) *****")
    print("Take turns with the PC to guess the number.\n")
    
    player_low, player_high = 1, 100
    pc_low, pc_high = 1, 100

    for round_num in range(attempts):
        print(f"\nRound {round_num + 1}")
        
        # Player's turn
        print("Your turn:")
        player_guess = int(input(f"Guess a number ({player_low}-{player_high}): "))
        if player_guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number}. You win!")
            return
        elif player_guess < secret_number:
            print("Too low!")
            player_low = max(player_low, player_guess + 1)
        else:
            print("Too high!")
            player_high = min(player_high, player_guess - 1)
        
        # PC's turn
        print("\nPC's turn:")
        pc_guess = random.randint(pc_low, pc_high)
        print(f"PC guesses: {pc_guess}")
        if pc_guess == secret_number:
            print(f"The PC guessed the secret number {secret_number}. PC wins!")
            return
        elif pc_guess < secret_number:
            print("PC's guess is too low!")
            pc_low = max(pc_low, pc_guess + 1)
        else:
            print("PC's guess is too high!")
            pc_high = min(pc_high, pc_guess - 1)

    print(f"\nNo one guessed the secret number. The number was {secret_number}. It's a draw!")

alternating_guessing_game()

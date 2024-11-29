import random

def game_with_history():
    """เกมที่บันทึกประวัติการเดาของผู้เล่น"""
    secret_number = random.randint(1, 100)
    attempts = 7
    history = []

    print("\n***** Guessing Game with History *****")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        history.append(guess)

        if guess == secret_number:
            print(f"Correct! You guessed the number {secret_number}.")
            print(f"Your guesses: {history}")
            return
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(f"\nGame over! The secret number was {secret_number}.")
    print(f"Your guesses: {history}")

game_with_history()

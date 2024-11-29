import random

def random_attempts_game():
    """เกมที่จำนวนรอบจะถูกสุ่ม"""
    secret_number = random.randint(1, 100)
    attempts = random.randint(3, 10)

    print(f"\n***** Random Attempts Guessing Game *****")
    print(f"You have {attempts} attempts to guess the number.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}.")
            return
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(f"\nGame over! The secret number was {secret_number}.")

random_attempts_game()

import random
import time

def time_limited_game():
    """เกมทายตัวเลขที่จำกัดเวลา"""
    secret_number = random.randint(1, 100)
    time_limit = 30  # 30 วินาที

    print("\n***** Time-Limited Guessing Game *****")
    print(f"You have {time_limit} seconds to guess the number.\n")
    start_time = time.time()

    while time.time() - start_time < time_limit:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}.")
            return
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(f"\nTime's up! The secret number was {secret_number}.")

time_limited_game()

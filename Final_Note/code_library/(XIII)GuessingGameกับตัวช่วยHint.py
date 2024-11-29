import random

def hint_guessing_game():
    """เกมที่มีตัวช่วยบอกระยะห่าง"""
    secret_number = random.randint(1, 100)
    attempts = 5

    print("\n***** Hint Guessing Game *****")
    print("Hints will tell you if you're very far, far, close, or very close.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        diff = abs(secret_number - guess)

        if guess == secret_number:
            print(f"Correct! You guessed the number {secret_number}.")
            return
        elif diff > 20:
            print("Hint: You're very far.")
        elif diff > 10:
            print("Hint: You're far.")
        elif diff > 5:
            print("Hint: You're close.")
        else:
            print("Hint: You're very close.")

    print(f"\nGame over! The secret number was {secret_number}.")

hint_guessing_game()

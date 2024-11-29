import random

def decoy_numbers_game():
    """เกมที่มีตัวเลขหลอกเพื่อทำให้ผู้เล่นไขว้เขว"""
    secret_number = random.randint(1, 100)
    decoy_numbers = random.sample(range(1, 101), 5)
    attempts = 7

    print("\n***** Decoy Numbers Guessing Game *****")
    print(f"The secret number is one of these: {decoy_numbers + [secret_number]}")

    for _ in range(attempts):
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}.")
            return
        elif guess in decoy_numbers:
            print(f"{guess} is a decoy! Keep trying.")
        else:
            print("Wrong guess!")

    print(f"\nGame over! The secret number was {secret_number}.")

decoy_numbers_game()

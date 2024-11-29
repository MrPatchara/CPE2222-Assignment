import random

def scoring_guessing_game():
    """เกมทายตัวเลขที่ให้คะแนนตามความใกล้เคียง"""
    secret_number = random.randint(1, 100)
    attempts = 5
    score = 0

    print("\n***** Scoring Guessing Game *****")
    print("Try to guess the number. The closer you are, the higher your score.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        diff = abs(secret_number - guess)
        points = max(0, 10 - diff)  # ยิ่งใกล้ยิ่งได้คะแนนสูงสุด 10
        score += points

        if guess == secret_number:
            print(f"Correct! You guessed the number {secret_number}.")
            break
        elif guess < secret_number:
            print(f"Your guess is too low. You scored {points} points.")
        else:
            print(f"Your guess is too high. You scored {points} points.")

    print(f"\nGame over! The secret number was {secret_number}. Total score: {score}")

scoring_guessing_game()

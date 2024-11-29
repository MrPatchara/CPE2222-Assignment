import random

def scoring_based_game():
    """เกมที่ผู้เล่นเริ่มด้วยคะแนนสูงสุดและลดลงตามจำนวนรอบ"""
    secret_number = random.randint(1, 100)
    max_score = 100
    attempts = 10

    print("\n***** Scoring-Based Guessing Game *****")
    print(f"Try to guess the number. You start with {max_score} points.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}.")
            print(f"Your score is {max_score}.")
            return
        else:
            max_score -= 10
            print("Wrong guess! Your score decreases.")

    print(f"\nGame over! The secret number was {secret_number}.")
    print(f"Your final score is {max_score}.")

scoring_based_game()

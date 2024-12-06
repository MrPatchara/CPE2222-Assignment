# โปรแกรมเกมทายตัวเลขที่จำนวนรอบจะเพิ่มขึ้นหรือลดลงตามความใกล้เคียง
import random

def adaptive_guessing_game():
    # เกมที่จำนวนรอบจะเพิ่มขึ้นหรือลดลงตามความใกล้เคียง
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    attempts = 5 # จำนวนรอบที่ให้ทาย

    print("\n***** Adaptive Guessing Game *****")
    print("Guess the number. Close guesses will give you more attempts!\n")

    while attempts > 0:
        print(f"Remaining attempts: {attempts}")
        guess = int(input("Enter your guess: "))
        diff = abs(secret_number - guess)

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}.")
            return
        elif diff <= 5:
            print("You're very close! You earned an extra attempt.")
            attempts += 1
        else:
            print("Keep trying!")
        attempts -= 1

    print(f"\nGame over! The secret number was {secret_number}.")

adaptive_guessing_game()

import random

def letter_range_game():
    """เกมที่ผู้เล่นต้องเดาช่วงของตัวเลขที่ซ่อนอยู่"""
    secret_number = random.randint(1, 100)
    attempts = 7
    ranges = {'A': (1, 25), 'B': (26, 50), 'C': (51, 75), 'D': (76, 100)}

    print("\n***** Letter-Range Guessing Game *****")
    print("Guess the range where the secret number belongs (A/B/C/D).")

    for _ in range(attempts):
        guess = input("Enter your range guess (A/B/C/D): ").upper()

        if guess in ranges:
            low, high = ranges[guess]
            if low <= secret_number <= high:
                print(f"Correct! The secret number {secret_number} is in range {guess}.")
                return
            else:
                print(f"Wrong! The secret number is not in range {guess}.")
        else:
            print("Invalid range. Choose A, B, C, or D.")

    print(f"\nGame over! The secret number was {secret_number}.")

letter_range_game()

# โปรแกรมเกมทายตัวเลขที่ขอบเขตการทายจะแคบลงตามรอบ
# โดยเริ่มต้นจาก 1-100 และลดลงเรื่อยๆ จนถึง 7 รอบ
import random

def shrinking_range_game():
    # เกมที่ขอบเขตการทายจะแคบลงตามรอบ
    secret_number = random.randint(1, 100)
    low, high = 1, 100 # ช่วงเริ่มต้น
    attempts = 7 # จำนวนรอบ

    print("\n***** Progressive Range Shrinking Game *****")
    print(f"The secret number is between {low} and {high}.\n")

    for _ in range(attempts):
        guess = int(input(f"Enter your guess ({low}-{high}): "))

        if guess == secret_number:
            print(f"Correct! The secret number is {secret_number}.")
            return
        elif guess < secret_number:
            print("Your guess is too low.")
            low = max(low, guess + 1)
        else:
            print("Your guess is too high.")
            high = min(high, guess - 1)

        print(f"New range: {low} to {high}")

    print(f"\nGame over! The secret number was {secret_number}.")

shrinking_range_game()

# โปรแกรมที่ใช้ในการเล่นเกมทายตัวเลข โดยมีจำนวนรอบที่ถูกกำหนดไว้ล่วงหน้า
import random

def random_attempts_game():
    # เกมที่จำนวนรอบจะถูกสุ่ม
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    attempts = random.randint(3, 10) # สุ่มจำนวนรอบที่ให้ทาย

    print(f"\n***** Random Attempts Guessing Game *****")
    print(f"You have {attempts} attempts to guess the number.\n")

    for attempt in range(1, attempts + 1): # วนลูปจนครบจำนวนรอบ
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number: # ถ้าทายถูก
            print(f"Congratulations! You guessed the number {secret_number}.")
            return
        elif guess < secret_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(f"\nGame over! The secret number was {secret_number}.")

random_attempts_game()

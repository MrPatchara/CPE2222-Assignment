# โปรแกรมเกมทายเลขที่บันทึกประวัติการเดาของผู้เล่น
# โดยให้ผู้เล่นทายเลขตั้งแต่ 1-100 โดยมีโอกาสทาย 7 ครั้ง
import random

def game_with_history():
    """เกมที่บันทึกประวัติการเดาของผู้เล่น"""
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    attempts = 7 # จำนวนรอบที่ให้ทาย
    history = [] # บันทึกประวัติการเดา

    print("\n***** Guessing Game with History *****")

    for attempt in range(1, attempts + 1): # วนลูปจนครบจำนวนรอบ
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        history.append(guess) # บันทึกประวัติการเดา

        if guess == secret_number: # ถ้าทายถูก
            print(f"Correct! You guessed the number {secret_number}.")
            print(f"Your guesses: {history}")
            return
        elif guess < secret_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือไม่
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(f"\nGame over! The secret number was {secret_number}.")
    print(f"Your guesses: {history}")

game_with_history()

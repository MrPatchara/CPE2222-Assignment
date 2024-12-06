# โปรแกรมทายตัวเลขที่ให้คะแนนตามความใกล้เคียง
import random

def scoring_guessing_game(): 
    # เกมทายตัวเลขที่ให้คะแนนตามความใกล้เคียง
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    attempts = 5 # จำนวนรอบที่ให้ทาย
    score = 0 # คะแนนเริ่มต้น

    print("\n***** Scoring Guessing Game *****")
    print("Try to guess the number. The closer you are, the higher your score.\n")

    for attempt in range(1, attempts + 1): # วนลูปจนครบจำนวนรอบ
        guess = int(input(f"Attempt {attempt}: Enter your guess: ")) # รับค่าที่ผู้เล่นทาย
        diff = abs(secret_number - guess) # คำนวณความต่างระหว่างตัวเลขที่ทายกับตัวเลขลับ
        points = max(0, 10 - diff)  # ยิ่งใกล้ยิ่งได้คะแนนสูงสุด 10
        score += points # บวกคะแนน

        if guess == secret_number: # ถ้าทายถูก
            print(f"Correct! You guessed the number {secret_number}.")
            break
        elif guess < secret_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
            print(f"Your guess is too low. You scored {points} points.")
        else: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
            print(f"Your guess is too high. You scored {points} points.")

    print(f"\nGame over! The secret number was {secret_number}. Total score: {score}")

scoring_guessing_game()

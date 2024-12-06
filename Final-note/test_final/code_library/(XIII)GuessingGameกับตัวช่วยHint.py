# โปรแกรมที่ใช้ในการเล่นเกมทายตัวเลข โดยมีตัวช่วยบอกระยะห่างของตัวเลขที่ทายไปจากตัวเลขที่ถูกต้อง
import random

def hint_guessing_game():
    # เกมที่มีตัวช่วยบอกระยะห่าง
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    attempts = 5 # จำนวนรอบที่ให้ทาย

    print("\n***** Hint Guessing Game *****")
    print("Hints will tell you if you're very far, far, close, or very close.\n")

    for attempt in range(1, attempts + 1): # วนลูปจนครบจำนวนรอบ
        guess = int(input(f"Attempt {attempt}: Enter your guess: ")) # รับค่าที่ผู้เล่นทาย
        diff = abs(secret_number - guess) # คำนวณความต่างระหว่างตัวเลขที่ทายกับตัวเลขลับ

        if guess == secret_number: # ถ้าทายถูก
            print(f"Correct! You guessed the number {secret_number}.")
            return
        elif diff > 20: # ถ้าความต่างมากกว่า 20
            print("Hint: You're very far.")
        elif diff > 10: # ถ้าความต่างมากกว่า 10
            print("Hint: You're far.")
        elif diff > 5: # ถ้าความต่างมากกว่า 5
            print("Hint: You're close.")
        else:
            print("Hint: You're very close.")

    print(f"\nGame over! The secret number was {secret_number}.")

hint_guessing_game()

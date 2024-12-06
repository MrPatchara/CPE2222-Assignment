# โปรแกรมเกมทายเลขที่มีการคิดคะแนน
import random

def scoring_guessing_game():
    random_number = random.randint(1, 99) # สุ่มตัวเลข
    attempts = 5 # จำนวนรอบที่ให้ทาย
    low, high = 1, 99 # ช่วงของตัวเลขที่ให้ทาย
    score = 100  # เริ่มต้นด้วยคะแนนเต็ม 100

    print("***** Welcome to the Scoring Guessing Game *****")

    for attempt in range(attempts): # วนลูปจนครบจำนวนรอบ
        print(f"{'-'*21} round{attempt + 1} {'-'*21}") # แสดงรอบที่เล่น
        print(f"Enter an integer from {low} to {high} : ", end="") # แสดงช่วงของตัวเลขที่ให้ทาย
        input_number = int(input()) # รับค่าที่ผู้เล่นทาย
        
        if input_number == random_number: # ถ้าทายถูก
            print("#" * 50)
            print("   *** CONGRATURATION *** Your guess is correct  ")
            print(f"Your final score is {score}")
            print("#" * 50)
            return
        else:
            diff = abs(input_number - random_number) # คำนวณความต่างระหว่างตัวเลขที่ทายกับตัวเลขลับ
            if diff <= 10: # ถ้าเดาใกล้
                score -= 5  # หัก 5 คะแนนถ้าเดาใกล้
                print("Close! But not quite.")
            else: # ถ้าเดาห่าง
                score -= 10  # หัก 10 คะแนนถ้าเดาห่าง
                print("Not even close!")

            if input_number < random_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
                print("Hint: Your guess is low")
                low = max(low, input_number + 1) 
            else:
                print("Hint: Your guess is high")
                high = min(high, input_number - 1)

    print("#" * 50)
    print(f"!!!SORRY!!! The secret number is {random_number}".center(50))
    print(f"Your final score is {score}".center(50))
    print("#" * 50)

scoring_guessing_game()

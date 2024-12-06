# โปรแกรมทายเลข 1-99 โดยมีโอกาสทาย 5 ครั้ง และให้คำแนะนำว่าเลขที่ทายมากไหม หรือน้อยไหม
# โดยโปรแกรมจะสุ่มเลข 1-99 และให้ผู้เล่นทาย โดยโปรแกรมจะให้คำแนะนำว่าเลขที่ทายมากไหม หรือน้อยไหม
import random

def guessing_game():
    random_number = random.randint(1, 99) # สุ่มเลข 1-99
    attempts = 5 # จำนวนรอบที่ให้ทาย
    low, high = 1, 99 # ช่วงที่เป็นไปได้

    print("***** Welcome to the game of guessing number *****")

    for attempt in range(attempts): # วนลูปจนครบจำนวนรอบ
        print(f"{'-'*21} round{attempt + 1} {'-'*21}") # แสดงรอบที่ทาย
        print(f"Enter an integer from {low} to {high} : ", end="") # รับค่าที่ต้องการทาย

        input_number = int(input()) # รับค่าที่ต้องการทาย

        if input_number == random_number: # ถ้าทายถูก
            print("#" * 50) 
            print("   *** CONGRATURATION *** Your guess is correct  ")
            print("#" * 50)
            return
        
        elif input_number < random_number: # ถ้าทายต่ำกว่าค่าที่สุ่ม
            print("Hint: Your guess is low")
            low = max(low, input_number + 1) # กำหนดช่วงที่เลือก
        else:
            print("Hint: Your guess is high")
            high = min(high, input_number - 1) # กำหนดช่วงที่เลือก

    print("#" * 50)
    print(f"!!!SORRY!!! The secret number is {random_number}".center(50))
    print("#" * 50)

guessing_game()

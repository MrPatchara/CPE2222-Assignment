# Assignment XIII: Guessing Game
import random #import module random

def guessing_game():
    print("***** Welcome to the game of guessing number *****")
    target = random.randint(1, 99)  #สุ่มตัวเลขจาก 1-99
    #target = 50 #ใช้เวลาจะทดสอบให้ถูก
    
    attempts = 5 #จำนวนครั้งในการทาย
    low, high = 1, 99 #กำหนดค่าต่ำสุดและสูงสุด

    for round_number in range(1, attempts + 1): #ทำการทายตั้งแต่ครั้งที่ 1 ถึง attempts
        print(f"-------------------round{round_number}--------------------")
        print(f"Enter an integer from {low} to {high} : ", end="") #ให้ผู้เล่นใส่ตัวเลขที่ต้องการทาย
        guess = int(input()) #รับค่าจากผู้เล่น
        
        if guess < target:
            print("Hint: Your guess is low")
            low = guess + 1  # Adjust the lower bound
        elif guess > target:
            print("Hint: Your guess is high")
            high = guess - 1  # Adjust the upper bound
        else:
            print("##############################################")
            print("*** CONGRATULATIONS *** Your guess is correct")
            print("##############################################")
            return  # End the game 

    
    print("##############################################")
    print("!!!Sorry!!! The secret number  is",{target})
    print("##############################################")

guessing_game()

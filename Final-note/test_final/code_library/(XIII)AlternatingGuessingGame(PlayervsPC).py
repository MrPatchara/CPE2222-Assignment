# โปรแกรมเกมทายตัวเลขที่ผู้เล่นและ PC สลับกันทาย ใครทายถูกก่อนชนะ
import random

def alternating_guessing_game():
    # เกมที่ผู้เล่นและ PC สลับกันทาย ใครทายถูกก่อนชนะ
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    attempts = 10 # จำนวนรอบที่ให้ทาย

    print("\n***** Alternating Guessing Game (Player vs PC) *****")
    print("Take turns with the PC to guess the number.\n")
    
    player_low, player_high = 1, 100 # ช่วงของตัวเลขที่ผู้เล่นสามารถทายได้
    pc_low, pc_high = 1, 100 # ช่วงของตัวเลขที่ PC สามารถทายได้

    for round_num in range(attempts): # วนลูปจนครบจำนวนรอบ
        print(f"\nRound {round_num + 1}") # แสดงรอบที่ทาย
        
        # Player's turn
        print("Your turn:")
        player_guess = int(input(f"Guess a number ({player_low}-{player_high}): ")) # ผู้เล่นทาย
        if player_guess == secret_number: # ถ้าทายถูก
            print(f"Congratulations! You guessed the secret number {secret_number}. You win!")
            return
        elif player_guess < secret_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
            print("Too low!")
            player_low = max(player_low, player_guess + 1) # ปรับช่วงของตัวเลขที่ผู้เล่นสามารถทายได้
        else:
            print("Too high!")
            player_high = min(player_high, player_guess - 1) # ปรับช่วงของตัวเลขที่ผู้เล่นสามารถทายได้
        
        # PC's turn
        print("\nPC's turn:")
        pc_guess = random.randint(pc_low, pc_high) # PC ทาย
        print(f"PC guesses: {pc_guess}") # แสดงการทายของ PC
        if pc_guess == secret_number:   # ถ้าทายถูก
            print(f"The PC guessed the secret number {secret_number}. PC wins!")
            return
        elif pc_guess < secret_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
            print("PC's guess is too low!")
            pc_low = max(pc_low, pc_guess + 1)
        else: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป 
            print("PC's guess is too high!")
            pc_high = min(pc_high, pc_guess - 1)

    print(f"\nNo one guessed the secret number. The number was {secret_number}. It's a draw!")

alternating_guessing_game()

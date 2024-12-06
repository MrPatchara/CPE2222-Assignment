# โปรแกรมทายตัวเลขแบบเล่นหลายคน
import random

def multiplayer_guessing_game():
    # เกมทายตัวเลขแบบเล่นหลายคน
    secret_number = random.randint(1, 100) # สุ่มตัวเลข
    max_attempts = 10 # จำนวนรอบที่ให้ทาย
    players = int(input("Enter number of players: ")) # จำนวนผู้เล่น
    attempts = {player: 0 for player in range(1, players + 1)} # จำนวนรอบการทายของแต่ละผู้เล่น

    print("\n***** Multiplayer Guessing Game *****")
    print(f"Secret number is between 1 and 100. Each player has {max_attempts} attempts.\n")

    for _ in range(max_attempts): # วนลูปจนครบจำนวนรอบ
        for player in range(1, players + 1):
            guess = int(input(f"Player {player}, enter your guess: "))
            attempts[player] += 1 # เพิ่มจำนวนรอบการทายของผู้เล่น

            if guess == secret_number: # ถ้าทายถูก
                print(f"\nPlayer {player} wins! The secret number was {secret_number}.")
                return
            elif guess < secret_number: # ตรวจสอบว่าเดาน้อยเกินไปหรือมากเกินไป
                print(f"Player {player}, your guess is too low.")
            else:
                print(f"Player {player}, your guess is too high.")

    print(f"\nGame over! The secret number was {secret_number}.")
    for player, attempt in attempts.items(): # แสดงจำนวนรอบการทายของแต่ละผู้เล่น
        print(f"Player {player} made {attempt} attempts.")

multiplayer_guessing_game()

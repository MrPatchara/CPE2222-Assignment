# เกม MEN and WOMEN แบบผู้เล่น 2 คน
import random

def generate_secret_number(): # ฟังก์ชันสร้างเลขที่ถูก
    """Generate a 4-digit secret number with unique digits."""
    return random.sample(range(10), 4) # สร้างเลขไม่ซ้ำ 4 ตัว

def calculate_hint(secret, guess): # ฟังก์ชันคำนวณ hint
    """Calculate MEN and WOMEN based on the guess."""
    men = sum(s == g for s, g in zip(secret, guess)) # นับ MEN โดยเทียบตำแหน่งและค่า
    women = sum(g in secret for g in guess) - men # WOMEN คือนับเลขที่อยู่ในคำตอบแต่ไม่ตรงตำแหน่ง
    return men, women # คืนค่า MEN และ WOMEN

print("------ Welcome to MEN and WOMEN number guessing game ------")
print("[Player 1 and Player 2 take turns to guess]")
print("[To exit the program, press 0]")
print("----------------------------------------------------------")

# สร้างเลขที่ถูกสำหรับผู้เล่นแต่ละคน
secret_number_p1 = generate_secret_number() # เลขของ Player 1
secret_number_p2 = generate_secret_number() # เลขของ Player 2

attempts_p1 = 0 # จำนวนครั้งที่ Player 1 ทาย
attempts_p2 = 0 # จำนวนครั้งที่ Player 2 ทาย

while True:
    # Player 1's turn
    print("\n--- Player 1's Turn ---")
    user_input_p1 = input("Player 1, enter 4-digits number: ")

    if user_input_p1 == "0": # ตรวจสอบว่าออกจากโปรแกรมหรือไม่
        print(f"Player 1's Secret Number was: {''.join(map(str, secret_number_p1))}")
        print(f"Player 2's Secret Number was: {''.join(map(str, secret_number_p2))}")
        print("Exiting the program.")
        break

    if len(user_input_p1) != 4 or not user_input_p1.isdigit(): # ตรวจสอบว่าป้อนตัวเลขถูกต้องหรือไม่
        print("Invalid input. Please enter a 4-digit number.")
        continue

    guess_p1 = list(map(int, user_input_p1)) # แปลงตัวเลขเป็น list
    if len(set(guess_p1)) != 4: # ตรวจสอบว่าเลขซ้ำกันหรือไม่
        print("Digits must be unique. Try again.")
        continue

    attempts_p1 += 1 # เพิ่มจำนวนครั้งที่ Player 1 ทาย
    men_p1, women_p1 = calculate_hint(secret_number_p2, guess_p1) # คำนวณ hint

    print(f"Hint for Player 1: MEN = {men_p1} and WOMEN = {women_p1}")

    if men_p1 == 4: # ถ้าทายถูกทั้งหมด
        print(f"*** Player 1 Wins *** Guessed correctly after {attempts_p1} attempts!")
        print(f"Player 2's Secret Number was: {''.join(map(str, secret_number_p2))}")
        break

    # Player 2's turn
    print("\n--- Player 2's Turn ---")
    user_input_p2 = input("Player 2, enter 4-digits number: ")

    if user_input_p2 == "0": # ตรวจสอบว่าออกจากโปรแกรมหรือไม่
        print(f"Player 1's Secret Number was: {''.join(map(str, secret_number_p1))}")
        print(f"Player 2's Secret Number was: {''.join(map(str, secret_number_p2))}")
        print("Exiting the program.")
        break

    if len(user_input_p2) != 4 or not user_input_p2.isdigit(): # ตรวจสอบว่าป้อนตัวเลขถูกต้องหรือไม่
        print("Invalid input. Please enter a 4-digit number.")
        continue

    guess_p2 = list(map(int, user_input_p2)) # แปลงตัวเลขเป็น list
    if len(set(guess_p2)) != 4: # ตรวจสอบว่าเลขซ้ำกันหรือไม่
        print("Digits must be unique. Try again.")
        continue

    attempts_p2 += 1 # เพิ่มจำนวนครั้งที่ Player 2 ทาย
    men_p2, women_p2 = calculate_hint(secret_number_p1, guess_p2) # คำนวณ hint

    print(f"Hint for Player 2: MEN = {men_p2} and WOMEN = {women_p2}")

    if men_p2 == 4: # ถ้าทายถูกทั้งหมด
        print(f"*** Player 2 Wins *** Guessed correctly after {attempts_p2} attempts!")
        print(f"Player 1's Secret Number was: {''.join(map(str, secret_number_p1))}")
        break
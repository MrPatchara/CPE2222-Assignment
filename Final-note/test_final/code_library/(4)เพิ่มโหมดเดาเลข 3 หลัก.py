# เกม MEN and WOMEN แบบ 3 หลัก
import random

def generate_secret_number(): # ฟังก์ชันสร้างเลขที่ถูก
    """Generate a 3-digit secret number with unique digits."""
    return random.sample(range(10), 3) # สร้างเลขไม่ซ้ำ 3 ตัว

def calculate_hint(secret, guess): # ฟังก์ชันคำนวณ hint
    """Calculate MEN and WOMEN based on the guess."""
    men = sum(s == g for s, g in zip(secret, guess)) # นับ MEN โดยเทียบตำแหน่งและค่า
    women = sum(g in secret for g in guess) - men # WOMEN คือนับเลขที่อยู่ในคำตอบแต่ไม่ตรงตำแหน่ง
    return men, women # คืนค่า MEN และ WOMEN

print("------ Welcome to MEN and WOMEN number guessing game (3 digits) ------")
print("[To exit the program, press 0]")
print("----------------------------------------------------------")

secret_number = generate_secret_number() # สร้างเลขที่ถูก
attempts = 0 # ตัวนับจำนวนครั้งที่ทาย

while True:
    user_input = input("Enter 3-digits number: ") # รับค่าจากผู้ใช้

    if user_input == "0": # ถ้าผู้ใช้ป้อน 0 ให้ออกจากโปรแกรม
        print(f"Secret Number was: {''.join(map(str, secret_number))}") # แสดงเลขที่ถูก
        print("Exiting the program.") # แสดงข้อความว่าออก
        break

    if len(user_input) != 3 or not user_input.isdigit(): # ตรวจสอบว่าผู้ใช้ป้อน 3 ตัวและเป็นตัวเลขหรือไม่
        print("Invalid input. Please enter a 3-digit number.") # แจ้งว่าผู้ใช้ป้อนผิด
        continue # วนลูปใหม่

    guess = list(map(int, user_input)) # แปลงค่าที่ผู้ใช้ป้อนเป็น list ของตัวเลข
    if len(set(guess)) != 3: # ตรวจสอบว่าเลขซ้ำหรือไม่
        print("Digits must be unique. Try again.") # แจ้งว่าต้องไม่ซ้ำ
        continue # วนลูปใหม่

    attempts += 1 # เพิ่มจำนวนครั้งที่ทาย
    men, women = calculate_hint(secret_number, guess) # คำนวณค่า MEN และ WOMEN

    print(f"Hint: MEN = {men} and WOMEN = {women}") # แสดงค่า MEN และ WOMEN

    if men == 3: # ถ้าทายถูกทั้งหมด
        print(f"*** Congratulations *** Your guess is correct, after {attempts} attempts") # แสดงข้อความแสดงความยินดี
        print(f"Secret Number was: {''.join(map(str, secret_number))}") # แสดงเลขที่ถูก
        break # ออกจากลูป
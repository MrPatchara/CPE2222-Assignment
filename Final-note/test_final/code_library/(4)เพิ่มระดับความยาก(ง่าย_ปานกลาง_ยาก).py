# เกม MEN and WOMEN โดยเพิ่มระดับความยากให้เลือก
import random

def generate_secret_number(length): # สร้างเลขที่ถูก
    """Generate a secret number with unique digits of specified length.""" # สร้างเลขที่ถูก
    return random.sample(range(10), length) # สร้างเลขที่ถูก

def calculate_hint(secret, guess): # คำนวณค่า hint
    """Calculate MEN and WOMEN based on the guess."""
    men = sum(s == g for s, g in zip(secret, guess)) # นับจำนวนที่ทายถูก
    women = sum(g in secret for g in guess) - men # นับจำนวนที่ทายผิด
    return men, women # คืนค่า

print("------ Welcome to MEN and WOMEN number guessing game ------")
print("[To exit the program, press 0]")
print("----------------------------------------------------------")

# เลือกระดับความยาก
difficulty = input("Choose difficulty level: Easy(4 digits), Medium(5 digits), Hard(6 digits): ").lower() # รับค่าจากผู้ใช้
if difficulty == "easy": # ถ้าเป็น easy จะเป็น 4 หลัก
    num_digits = 4
elif difficulty == "medium": # ถ้าเป็น medium จะเป็น 5 หลัก
    num_digits = 5
else:
    num_digits = 6 # ถ้าไม่ใช่ easy หรือ medium จะเป็น hard

secret_number = generate_secret_number(num_digits) # สร้างเลขที่ถูก
attempts = 0 # จำนวนครั้งที่ทาย

while True:
    user_input = input(f"Enter {num_digits}-digit number: ") # รับค่าจากผู้ใช้

    if user_input == "0": # ถ้าใส่ 0 จะออกจากโปรแกรม
        print(f"Secret Number was: {''.join(map(str, secret_number))}") # แสดงเลขที่ถูก
        print("Exiting the program.") # แสดงข้อความว่าออก
        break

    if len(user_input) != num_digits or not user_input.isdigit(): # ตรวจสอบว่าเป็นตัวเลขหรือไม่
        print(f"Invalid input. Please enter a {num_digits}-digit number.") # แสดงข้อความว่าใส่ผิด
        continue

    guess = list(map(int, user_input)) # แปลงข้อมูลให้เป็น list
    if len(set(guess)) != num_digits: # ตรวจสอบว่าเลขซ้ำกันหรือไม่
        print("Digits must be unique. Try again.") # แสดงข้อความว่าใส่ซ้ำ
        continue # วน loop ใหม่

    attempts += 1 # นับจำนวนครั้งที่ทาย
    men, women = calculate_hint(secret_number, guess) # คำนวณค่า hint

    print(f"Hint: MEN = {men} and WOMEN = {women}") # แสดงค่า hint

    if men == num_digits: # ถ้าทายถูกทุกตัว
        print(f"*** Congratulations *** Your guess is correct, after {attempts} attempts") # แสดงข้อความว่าถูก
        print(f"Secret Number was: {''.join(map(str, secret_number))}") # แสดงเลขที่ถูก
        break
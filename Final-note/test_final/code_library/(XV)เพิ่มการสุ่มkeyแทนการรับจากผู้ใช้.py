# โปรแกรมที่ใช้สร้าง key และเข้ารหัสข้อความด้วย key ที่สร้างขึ้น
import random

def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a') # ตรวจสอบว่าเป็นตัวพิมพ์ใหญ่หรือเล็ก
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base) # คำนวณตำแหน่งของตัวอักษรที่ถูกเข้ารหัส
            result += shifted_char # ต่อค่าที่ถูกเข้ารหัสเข้ากับตัวแปร
        else:
            raise ValueError("Error!!!! Input non-characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = random.randint(1, 25)  # Generate a random key between 1 and 25
    print(f"Generated secret key: {key}")

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

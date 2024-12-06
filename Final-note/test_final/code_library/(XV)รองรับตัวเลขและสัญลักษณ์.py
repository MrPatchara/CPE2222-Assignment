# โปรแกรมเข้ารหัสข้อความด้วยวิธี Caesar Cipher
def secret_password(text, key): # ฟังก์ชันเข้ารหัสข้อความ
    result = ""
    for char in text: # วนลูปทุกตัวอักษรในข้อความ
        if char.isalpha(): # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            shift_base = ord('A') if char.isupper() else ord('a') # กำหนดตัวอักษรฐาน
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base) # คำนวณตัวอักษรที่ถูกเข้ารหัส
            result += shifted_char # เก็บตัวอักษรที่ถูกเข้ารหัส
        elif char.isdigit(): # ตรวจสอบว่าเป็นตัวเลขหรือไม่
            shifted_digit = (int(char) + key) % 10 # คำนวณตัวเลขที่ถูกเข้ารหัส
            result += str(shifted_digit) # เก็บตัวเลขที่ถูกเข้ารหัส
        elif char in "!@#$%^&*()-_=+[]{};:,.<>?/": # ตรวจสอบว่าเป็นสัญลักษณ์หรือไม่
            shifted_special = chr((ord(char) + key) % 256)  # คำนวณสัญลักษณ์ที่ถูกเข้ารหัส
            result += shifted_special # เก็บสัญลักษณ์ที่ถูกเข้ารหัส
        elif char.isspace(): # ตรวจสอบว่าเป็นช่องว่างหรือไม่
            result += char # เก็บช่องว่างไว้
        else:
            raise ValueError("Error!!!! Input contains unsupported characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabets, Digits, Special Characters): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key) # เรียกใช้ฟังก์ชันเข้ารหัสข้อความ
    print("The encrypted ciphertext:", ciphertext) # แสดงข้อความที่ถูกเข้ารหัส

    decrypted_text = secret_password(ciphertext, -key) # เรียกใช้ฟังก์ชันถอดรหัสข้อความ
    print(f'The decryption result: {decrypted_text}') # แสดงข้อความที่ถูกถอดรหัส
except ValueError as e:
    print(e)

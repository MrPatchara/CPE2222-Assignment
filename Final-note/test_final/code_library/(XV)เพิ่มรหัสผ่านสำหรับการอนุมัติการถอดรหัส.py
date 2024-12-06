# โปรแกรมเข้ารหัสข้อความด้วยวิธี Caesar Cipher และถอดรหัสด้วยรหัสผ่าน
def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha(): # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            shift_base = ord('A') if char.isupper() else ord('a') # ตรวจสอบว่าเป็นตัวพิมพ์ใหญ่หรือเล็ก
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base) # คำนวณตำแหน่งของตัวอักษรที่ถูกเข้ารหัส
            result += shifted_char # ต่อค่าที่ถูกเข้ารหัสเข้ากับตัวแปร
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))
    password = input("Set a password for decryption: ")

    # เข้ารหัสข้อความ
    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    # ตรวจสอบรหัสผ่านก่อนถอดรหัส
    input_password = input("Enter password to decrypt: ")
    if input_password == password: # ถ้ารหัสผ่านถูกต้อง
        decrypted_text = secret_password(ciphertext, -key) # ถอดรหัสข้อความ
        print(f'The decryption result: {decrypted_text}') # แสดงผลลัพธ์
    else:
        print("Error: Invalid password!")
except ValueError as e:
    print(e)

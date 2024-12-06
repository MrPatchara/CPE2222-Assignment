# โปรแกรมเข้ารหัสข้อความด้วยวิธีการเข้ารหัส Caesar Cipher โดยให้ผู้ใช้ป้อนข้อความและคีย์เป็นจำนวนเต็มบวกหรือลบ
def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            shift_base = ord('A') if char.isupper() else ord('a') # ตรวจสอบว่าเป็นตัวพิมพ์ใหญ่หรือเล็ก
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base) # คำนวณตำแหน่งของตัวอักษรที่ถูกเข้ารหัส
            result += shifted_char # ต่อค่าที่ถูกเข้ารหัสเข้ากับตัวแปร
        elif char.isdigit():  # ตรวจสอบว่าเป็นตัวเลขหรือไม่
            shifted_digit = (int(char) + key) % 10 # คำนวณตำแหน่งของตัวเลขที่ถูกเข้ารหัส
            result += str(shifted_digit) # ต่อค่าที่ถูกเข้ารหัสเข้ากับตัวแปร
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabets and Digits Only): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

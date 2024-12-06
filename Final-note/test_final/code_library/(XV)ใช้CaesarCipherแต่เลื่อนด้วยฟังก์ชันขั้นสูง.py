# โปรแกรมที่ใช้เข้ารหัสและถอดรหัสข้อความโดยใช้วิธีการเลื่อนตัวอักษรโดยใช้ฟังก์ชัน sin
# โดยใช้ความซับซ้อนในการเลื่อนตัวอักษรโดยใช้ฟังก์ชัน sin ในการเลื่อนตัวอักษร
import math

def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # เลื่อนตัวอักษรโดยใช้ฟังก์ชัน sin เพื่อเพิ่มความซับซ้อน
            adjusted_key = math.floor(key + math.sin(ord(char)) * 5)
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + adjusted_key) % 26 + shift_base)
            result += shifted_char
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    # เข้ารหัสโดยใช้ฟังก์ชัน sin ในการเลื่อนตัวอักษร
    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    # ถอดรหัสกลับโดยใช้ key เดิม
    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

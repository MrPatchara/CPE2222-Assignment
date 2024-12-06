# โปรแกรมที่ใช้ในการเข้ารหัสและถอดรหัสข้อความด้วยวิธี Caesar Cipher และใช้ Base64 เป็นวิธีการเข้ารหัสข้อความที่เข้ารหัสแล้ว
import base64

def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    # ขั้นตอนการเข้ารหัส
    encrypted_text = secret_password(plaintext, key)
    
    # แปลงข้อความที่เข้ารหัสไปเป็น Base64
    base64_encoded = base64.b64encode(encrypted_text.encode()).decode() # แปลงข้อความที่เข้ารหัสไปเป็น Base64
    print("The encrypted ciphertext (Base64):", base64_encoded) # แสดงข้อความที่ถูกเข้ารหัสแล้ว

    # ถอดรหัสจาก Base64 ก่อน
    base64_decoded = base64.b64decode(base64_encoded).decode() # ถอดรหัสจาก Base64

    # ถอดรหัสกลับด้วย key เดิม
    decrypted_text = secret_password(base64_decoded, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

#คำสั่ง import base64 ในภาษา Python คือการนำเข้า (import) โมดูล base64 ที่ใช้สำหรับการเข้ารหัสและถอดรหัสข้อมูลในรูปแบบ Base64 ซึ่งเป็นเทคนิคที่ใช้ในการแปลงข้อมูลจากรูปแบบไบต์ (binary) ให้เป็นข้อความในรูปแบบที่สามารถแสดงผลได้เป็นข้อความ ASCII ตัวอักษร
#Base64 มักจะใช้ในการถ่ายโอนข้อมูลที่เป็นไบต์ เช่น ภาพหรือไฟล์ในรูปแบบที่ไม่สามารถแสดงผลได้โดยตรงในข้อความ (เช่น ไฟล์อีเมลหรือ HTTP requests) เพื่อให้สามารถส่งข้อมูลผ่านทางช่องทางที่รองรับเฉพาะข้อความ ASCII ได้

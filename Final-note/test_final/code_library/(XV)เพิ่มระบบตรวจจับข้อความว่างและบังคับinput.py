# โปรแกรมที่ใช้ในการเข้ารหัสข้อความด้วยวิธี Caesar cipher โดยใช้ key ที่กำหนดให้
def secret_password(text, key): # ฟังก์ชันเข้ารหัสข้อความ
    result = "" # ตัวแปรสำหรับเก็บข้อความที่ถูกเข้ารหัส
    for char in text: # วนลูปทุกตัวอักษรในข้อความ
        if char.isalpha():  # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            shift_base = ord('A') if char.isupper() else ord('a')  # กำหนดตัวอักษรฐาน
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)  # คำนวณตัวอักษรที่ถูกเข้ารหัส/ถอดรหัส
            result += shifted_char  # เพิ่มตัวอักษรที่ถูกเข้ารหัส/ถอดรหัส
        elif char.isspace():  # สงวนช่องว่างในข้อความ
            result += char
        else:  # สร้างข้อผิดพลาดหากพบตัวอักษรที่ไม่รองรับ
            raise ValueError("ข้อผิดพลาด!!!! ข้อมูลนำเข้ามีตัวอักษรที่ไม่รองรับ.")
    return result

try:
    # แสดงข้อความให้ผู้ใช้กรอกข้อความที่ถูกต้อง
    while True:
        plaintext = input("กรุณากรอกข้อความ (เฉพาะตัวอักษรเท่านั้น, ไม่เป็นค่าว่าง): ").strip()
        if plaintext:  # ตรวจสอบว่าข้อมูลนำเข้าไม่เป็นค่าว่าง
            break
        print("ข้อผิดพลาด: ข้อความต้องไม่เป็นค่าว่าง กรุณาลองอีกครั้ง.")
    
    # แสดงข้อความให้ผู้ใช้กรอกคีย์ที่ถูกต้อง
    key = int(input("กรุณากรอกคีย์ลับ (ตัวเลขเท่านั้น): "))

    # เข้ารหัสข้อความ
    ciphertext = secret_password(plaintext, key)
    print("ข้อความที่ถูกเข้ารหัส:", ciphertext)

    # ถอดรหัสข้อความ
    decrypted_text = secret_password(ciphertext, -key)
    print(f'ผลลัพธ์การถอดรหัส: {decrypted_text}')
except ValueError as e:
    print(e)

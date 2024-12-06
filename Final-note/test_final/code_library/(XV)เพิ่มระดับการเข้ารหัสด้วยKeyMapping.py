# โปรแกรมที่ใช้ในการเข้ารหัสข้อความด้วยวิธีการเข้ารหัสแบบ Caesar Cipher โดยมีการกำหนดค่า key ที่ใช้ในการเข้ารหัส
def secret_password_with_mapping(text, key_mapping):
    result = ""
    for char in text:
        if char.isalpha(): # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            result += key_mapping.get(char, char)  # เปลี่ยนตัวอักษรโดยใช้ key_mapping
        elif char.isspace(): # สงวนช่องว่าง
            result += char  # สงวนช่องว่าง
        else:
            raise ValueError("ข้อผิดพลาด!!!! ข้อมูลนำเข้ามีตัวอักษรที่ไม่รองรับ")
    return result

try:
    plaintext = input("ป้อนข้อความที่ต้องการเข้ารหัส (เฉพาะตัวอักษร): ")
    key = int(input("ป้อนคีย์ลับ (เฉพาะตัวเลข): "))

    # สร้าง key mapping สำหรับตัวอักษรตัวพิมพ์ใหญ่และตัวพิมพ์เล็ก
    key_mapping = {}
    for i in range(26):
        key_mapping[chr(ord('A') + i)] = chr((ord('A') + i - ord('A') + key) % 26 + ord('A')) # ตัวอักษรตัวพิมพ์ใหญ่
        key_mapping[chr(ord('a') + i)] = chr((ord('a') + i - ord('a') + key) % 26 + ord('a')) # ตัวอักษรตัวพิมพ์เล็ก

    # เข้ารหัสและแสดงผลลัพธ์
    ciphertext = secret_password_with_mapping(plaintext, key_mapping) # เข้ารหัสข้อความ
    print("ข้อความที่เข้ารหัส:", ciphertext) # แสดงข้อความที่เข้ารหัส

    # กลับด้าน key mapping เพื่อถอดรหัส
    reverse_mapping = {v: k for k, v in key_mapping.items()} # กลับด้าน key mapping
    decrypted_text = secret_password_with_mapping(ciphertext, reverse_mapping) # ถอดรหัสข้อความ
    print(f'ผลลัพธ์การถอดรหัส: {decrypted_text}') # แสดงข้อความที่ถอดรหัส
except ValueError as e:
    print(e)

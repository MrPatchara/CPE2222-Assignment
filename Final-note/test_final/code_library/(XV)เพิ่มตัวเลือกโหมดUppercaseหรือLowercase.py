# โปรแกรมเข้ารหัสและถอดรหัสข้อความที่มีตัวอักษรเท่านั้น โดยใช้วิธีการเข้ารหัสแบบ Caesar Cipher โดยมีการเลือกโหมดการทำงาน 3 แบบ คือ
def secret_password(text, key, mode="normal"): # ฟังก์ชันเข้ารหัสข้อความด้วยวิธี Caesar Cipher
    result = ""
    for char in text: # วนลูปตามตัวอักษรในข้อความ
        if char.isalpha(): # ตรวจสอบว่าเป็นตัวอักษรหรือไม่
            shift_base = ord('A') if char.isupper() else ord('a') # ตรวจสอบว่าเป็นตัวพิมพ์ใหญ่หรือเล็ก
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base) # คำนวณตำแหน่งของตัวอักษรที่ถูกเข้ารหัส
            if mode == "uppercase": # ตรวจสอบโหมดการทำงาน
                shifted_char = shifted_char.upper() # แปลงเป็นตัวพิมพ์ใหญ่
            elif mode == "lowercase": # ตรวจสอบโหมดการทำงาน
                shifted_char = shifted_char.lower() # แปลงเป็นตัวพิมพ์เล็ก
            result += shifted_char # ต่อค่าท
        else:
            raise ValueError("Error!!!! Input non-characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))
    mode = input("Choose mode (normal/uppercase/lowercase): ").strip().lower() # รับโหมดการทำงาน

    ciphertext = secret_password(plaintext, key, mode) # เข้ารหัสข้อความ
    print("The encrypted ciphertext:", ciphertext) # แสดงข้อความที่ถูกเข้ารหัส

    decrypted_text = secret_password(ciphertext, -key, mode) # ถอดรหัสข้อความ
    print(f'The decryption result: {decrypted_text}') # แสดงผลลัพธ์
except ValueError as e:
    print(e)

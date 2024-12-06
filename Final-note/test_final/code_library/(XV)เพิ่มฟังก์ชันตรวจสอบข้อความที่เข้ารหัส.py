# โปรแกรมเข้ารหัสข้อความด้วยวิธี Caesar Cipher โดยใช้ key เป็นจำนวนเต็มบวกหรือลบ
def is_valid_encrypted(text, key): # ฟังก์ชันตรวจสอบว่าข้อความที่ถูกเข้ารหัสสามารถถอดรหัสกลับได้หรือไม่
    try:
        # พยายามถอดรหัสข้อความ หากไม่เกิด Error แปลว่าเป็นข้อความที่ถูกต้อง
        decrypted = secret_password(text, -key) # ถอดรหัสข้อความ
        return True # ถ้าถอดรหัสได้สำเร็จแสดงว่าเป็นข้อความที่ถูกต้อง
    except:
        return False # ถ้าเกิด Error แสดงว่าเป็นข้อความที่ไม่ถูกต้อง

def secret_password(text, key): # ฟังก์ชันเข้ารหัสข้อความด้วยวิธี Caesar Cipher
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

    # เข้ารหัสข้อความ
    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    # ตรวจสอบว่าข้อความที่เข้ารหัสสามารถถอดกลับได้หรือไม่
    if is_valid_encrypted(ciphertext, key):
        print("The ciphertext is valid and can be decrypted!")
    else:
        print("The ciphertext is invalid.")
except ValueError as e:
    print(e)

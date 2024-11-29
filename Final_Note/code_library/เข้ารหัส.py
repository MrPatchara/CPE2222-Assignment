# ข้อความต้นฉบับ
s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing."

# ฟังก์ชันเข้ารหัส Caesar Cipher
def caesar_cipher(text, shift):
    """
    ฟังก์ชันสำหรับเข้ารหัสข้อความด้วย Caesar Cipher
    - text: ข้อความที่ต้องการเข้ารหัส
    - shift: จำนวนตำแหน่งที่ต้องการเลื่อนอักขระ
    """
    result = ""
    for char in text:
        if char.isalpha():  # ตรวจสอบว่าเป็นตัวอักษร
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # ถ้าไม่ใช่ตัวอักษร ให้คงเดิม
    return result

# ======================= การวิเคราะห์ข้อความ ======================= #

# จำนวนตัวอักษรทั้งหมดใน s1, s2, s3
total_char = len(s1) + len(s2) + len(s3)
print(f"Total characters: {total_char}")

# จำนวนคำทั้งหมดใน s1, s2, s3
total_words = len(s1.split()) + len(s2.split()) + len(s3.split())
print(f"Total words: {total_words}")

# ======================= การเข้ารหัสลับ ======================= #

# เข้ารหัสข้อความแต่ละส่วน
shift_value = 5  # จำนวนตำแหน่งที่เลื่อน
encoded_s1 = caesar_cipher(s1, shift_value)
encoded_s2 = caesar_cipher(s2, shift_value)
encoded_s3 = caesar_cipher(s3, shift_value)

print("\nEncoded Strings:")
print(f"Encoded s1: {encoded_s1}")
print(f"Encoded s2: {encoded_s2}")
print(f"Encoded s3: {encoded_s3}")

# ======================= การสร้างรหัสลับ ======================= #

# ใช้ตัวอักษรบางตัวจากข้อความเข้ารหัสเป็น "รหัสลับ"
secret_code = encoded_s1[10] + encoded_s2[15] + encoded_s3[20]
print(f"\nThe secret code is: {secret_code}")

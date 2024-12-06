# โปรแกรมเข้ารหัสข้อความด้วยวิธีการเข้ารหัส Caesar Cipher โดยใช้ Unicode
# โปรแกรมเข้ารหัสข้อความด้วยวิธี Caesar Cipher โดยให้ผู้ใช้ป้อนข้อความและคีย์เป็นจำนวนเต็มบวกหรือลบ
def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        elif char.isspace():  # Allow spaces between words
            result += ' '
        else:  # Convert special characters to Unicode
            result += f"\\u{ord(char):04x}"
    return result

try:
    plaintext = input("Enter plaintext (Alphabets, Spaces, or Special Characters): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

#Unicode คือระบบการเข้ารหัส (encoding system) ที่ใช้เพื่อแทนข้อมูลตัวอักษรหรือสัญลักษณ์ต่างๆ ที่สามารถใช้ได้ในทุกภาษาและทุกสัญลักษณ์ทั่วโลก เช่น ตัวอักษรในภาษาอังกฤษ, ภาษาไทย, ภาษาจีน, อีโมจิ หรือแม้กระทั่งสัญลักษณ์พิเศษต่างๆ
#เป้าหมายของ Unicode: การพัฒนา Unicode มีจุดมุ่งหมายเพื่อให้สามารถแทนข้อมูลข้อความจากทุกภาษาในโลกได้ในมาตรฐานเดียวกัน โดยไม่ต้องใช้ระบบการเข้ารหัสหลายแบบที่แตกต่างกัน ซึ่งอาจทำให้เกิดปัญหาการไม่สามารถแสดงผลตัวอักษรที่ต้องการได้ (เช่น ปัญหาการแสดงผลภาษาไทยในระบบที่ใช้การเข้ารหัสเป็น ASCII)
#รหัสของ Unicode: Unicode แทนตัวอักษรแต่ละตัว (หรือสัญลักษณ์) ด้วยรหัสที่เรียกว่า code point ซึ่งเป็นตัวเลขที่ไม่ซ้ำกัน ซึ่งสามารถเป็นตัวเลขที่ใหญ่และสามารถแทนข้อมูลได้หลากหลายประเภทของตัวอักษร เช่น:
#รหัสตัวอักษรภาษาอังกฤษ: เช่น U+0041 (A), U+0042 (B) เป็นต้น
#รหัสตัวอักษรภาษาไทย: เช่น U+0E01 (ก), U+0E02 (ข) เป็นต้น
#สัญลักษณ์พิเศษ: เช่น U+1F600 (😀), U+1F602 (😂) เป็นต้น
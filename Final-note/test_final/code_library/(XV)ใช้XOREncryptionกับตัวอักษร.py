# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR
# โดยใช้ฟังก์ชัน secret_password(text, key) ที่รับข้อความและคีย์เป็นอาร์กิวเมนต์
def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # ใช้ XOR กับ key เพื่อเข้ารหัสตัวอักษร
            shifted_char = chr(ord(char) ^ key)  
            result += shifted_char
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    # เข้ารหัสข้อความด้วย XOR
    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    # ถอดรหัสข้อความด้วย XOR (กระบวนการเดียวกันเพราะ XOR เป็นการกลับด้านได้)
    decrypted_text = secret_password(ciphertext, key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

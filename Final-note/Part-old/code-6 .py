# 6.จงเขียนโปรแกรมรับค่าการนำข้อมูล ( Plaintext) และทำการรับค่าตัวเลขเป็นกุญแจลับ ( Secret Key)
# ฟังก์ชั่นเพื่อเข้ารหัสและถอดรหัสโดยใช้ XOR
def xor_cipher(plaintext, secret_key):
    # ปรับขนาดของ Secret Key
    if len(plaintext) > len(secret_key):
        # ถ้า Plaintext ยาวกว่า Secret Key ให้ทำการวน Secret Key
        secret_key = (secret_key * ((len(plaintext) // len(secret_key)) + 1))[:len(plaintext)]
    elif len(plaintext) < len(secret_key):
        # ถ้า Secret Key ยาวกว่า Plaintext ให้ตัด Secret Key
        secret_key = secret_key[:len(plaintext)]
    
    # การเข้ารหัสลับโดยการ XOR
    ciphertext = ''.join([chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, secret_key)])
    
    # การถอดรหัสลับคือการ XOR อีกครั้ง
    decrypted_text = ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, secret_key)])
    
    # แปลง Ciphertext เป็น Hex
    ciphertext_hex = ' '.join(f'{ord(c):02x}' for c in ciphertext)
    
    return ciphertext, ciphertext_hex, decrypted_text

# รับค่า Plaintext และ Secret Key จากผู้ใช้
plaintext = input("Enter your plaintext: ")
print(f"The length of plaintext is {len(plaintext)} characters")

secret_key = input("Enter your secret key: ")
print(f"The length of secret key is {len(secret_key)} characters")

# คำนวณ Ciphertext และ Decryption Results
ciphertext, ciphertext_hex, decrypted_text = xor_cipher(plaintext, secret_key)

# แสดงผลลัพธ์
print(f"The encrypted ciphertext : {ciphertext}")
print(f"The encrypted ciphertext (Hex): {ciphertext_hex}")
print(f"The length of ciphertext is {len(ciphertext)} characters")
print(f"The decryption results: {decrypted_text}\n")

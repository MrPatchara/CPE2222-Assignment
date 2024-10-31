# Assignment XV 15
# รับข้อความจากผู้ใช้ (plaintext) ซึ่งต้องเป็นตัวอักษร (alphabet only) และรับค่าหมายเลข (secret key) ที่จะใช้ในการเข้ารหัส
plaintext = input("Enter your plaintext (Alphabet Only): ")
secretkey = int(input("Enter your secret key (Number Only): "))

# ฟังก์ชันเข้ารหัส 
def encrypt(P, k):
    result = "" # สร้างตัวแปรเพื่อเก็บข้อความที่เข้ารหัส
    for char in P: # วนลูปทุกตัวอักษรในข้อความ
        if char.isupper(): # ถ้าเป็นตัวพิมพ์ใหญ่
            result += chr((ord(char) - 65 + k) % 26 + 65) # เข้ารหัสตัวอักษรตัวพิมพ์ใหญ่
        elif char.islower(): # ถ้าเป็นตัวพิมพ์เล็ก
            result += chr((ord(char) - 97 + k) % 26 + 97) # เข้ารหัสตัวอักษรตัวพิมพ์เล็ก
    return result

# ฟังก์ชันถอดรหัส 
def decrypt(C, k):
    result = "" # สร้างตัวแปรเพื่อเก็บข้อความที่ถอดรหัส
    for char in C: # วนลูปทุกตัวอักษรในข้อความ
        if char.isupper(): # ถ้าเป็นตัวพิมพ์ใหญ่
            result += chr((ord(char) - 65 - k) % 26 + 65) # ถอดรหัสตัวอักษรตัวพิมพ์ใหญ่
        elif char.islower(): # ถ้าเป็นตัวพิมพ์เล็ก
            result += chr((ord(char) - 97 - k) % 26 + 97) # ถอดรหัสตัวอักษรตัวพิมพ์เล็ก
    return result

# เข้ารหัสข้อความ
ciphertext = encrypt(plaintext, secretkey) 
print('The encrypted ciphertext:', ciphertext) 

# ถอดรหัสข้อความ
decryptedtext = decrypt(ciphertext, secretkey)
print('The decryption results:', decryptedtext)

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
    base64_encoded = base64.b64encode(encrypted_text.encode()).decode()
    print("The encrypted ciphertext (Base64):", base64_encoded)

    # ถอดรหัสจาก Base64 ก่อน
    base64_decoded = base64.b64decode(base64_encoded).decode()

    # ถอดรหัสกลับด้วย key เดิม
    decrypted_text = secret_password(base64_decoded, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

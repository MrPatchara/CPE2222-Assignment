def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        elif char.isspace():  # Space characters remain unchanged
            result += ' '
        else:  # Convert special characters to Unicode
            result += f"\\u{ord(char):04x}"
    return result

def reverse_alphabet_encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            reversed_char = chr(shift_base + (25 - (ord(char) - shift_base)))
            result += reversed_char
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

def hybrid_encrypt(text, key):
    # เข้ารหัสแบบ Caesar
    encrypted_text = secret_password(text, key)
    # เปลี่ยนไปใช้ Reverse Alphabet
    return reverse_alphabet_encrypt(encrypted_text)

def hybrid_decrypt(text, key):
    # ถอดรหัสจาก Reverse Alphabet
    decrypted_text = reverse_alphabet_encrypt(text)
    # ถอดรหัสจาก Caesar
    return secret_password(decrypted_text, -key)

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    # เข้ารหัสแบบ Hybrid
    ciphertext = hybrid_encrypt(plaintext, key)
    print("The hybrid encrypted ciphertext:", ciphertext)

    # ถอดรหัสข้อความแบบ Hybrid
    decrypted_text = hybrid_decrypt(ciphertext, key)
    print(f'The hybrid decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

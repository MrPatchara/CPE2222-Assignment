from datetime import datetime

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
    time_based_key = datetime.now().second % 26  # ใช้วินาทีเป็น key เสริม
    print(f"Time-based key is: {time_based_key}")
    
    key = int(input("Enter secret key (Number Only): "))
    combined_key = key + time_based_key

    # เข้ารหัสด้วย key ผสม
    ciphertext = secret_password(plaintext, combined_key)
    print("The encrypted ciphertext:", ciphertext)

    # ถอดรหัสด้วยการใช้ key ผสมกลับ
    decrypted_text = secret_password(ciphertext, -(combined_key))
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

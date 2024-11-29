def is_valid_encrypted(text, key):
    try:
        # พยายามถอดรหัสข้อความ หากไม่เกิด Error แปลว่าเป็นข้อความที่ถูกต้อง
        decrypted = secret_password(text, -key)
        return True
    except:
        return False

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

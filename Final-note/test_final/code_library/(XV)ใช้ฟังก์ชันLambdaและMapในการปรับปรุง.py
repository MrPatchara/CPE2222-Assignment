# โปรแกรมรับข้อความและคีย์จากผู้ใช้ แล้วทำการเข้ารหัสข้อความด้วยวิธี Caesar Cipher และแสดงผลลัพธ์ข้อความที่เข้ารหัส
def shift_char(char, key):
    if char.isalpha():
        shift_base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - shift_base + key) % 26 + shift_base)
    elif char.isspace():
        return char
    else:
        raise ValueError("Error!!!! Input contains invalid characters.")

def secret_password(text, key):
    return ''.join(map(lambda char: shift_char(char, key), text))

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

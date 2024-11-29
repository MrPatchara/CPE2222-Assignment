def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        else:
            raise ValueError("Error!!!! Input non-characters.")
    return result

def repeat_encrypt(text, key, rounds):
    for _ in range(rounds):
        text = secret_password(text, key)
    return text

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))
    rounds = int(input("Enter number of encryption rounds: "))

    # เข้ารหัสข้อความแบบวนซ้ำ
    ciphertext = repeat_encrypt(plaintext, key, rounds)
    print(f"The encrypted ciphertext after {rounds} rounds:", ciphertext)

    # ถอดรหัสแบบวนซ้ำกลับ
    decrypted_text = repeat_encrypt(ciphertext, -key, rounds)
    print(f'The decryption result after {rounds} rounds: {decrypted_text}')
except ValueError as e:
    print(e)

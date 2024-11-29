import random

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

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = random.randint(1, 25)  # Generate a random key between 1 and 25
    print(f"Generated secret key: {key}")

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

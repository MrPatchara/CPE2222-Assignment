def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        elif char.isdigit():
            shifted_digit = (int(char) + key) % 10
            result += str(shifted_digit)
        elif char in "!@#$%^&*()-_=+[]{};:,.<>?/":
            shifted_special = chr((ord(char) + key) % 256)  # Shift symbols
            result += shifted_special
        elif char.isspace():
            result += char
        else:
            raise ValueError("Error!!!! Input contains unsupported characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabets, Digits, Special Characters): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

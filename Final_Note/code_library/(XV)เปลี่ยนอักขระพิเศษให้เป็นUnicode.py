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

try:
    plaintext = input("Enter plaintext (Alphabets, Spaces, or Special Characters): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

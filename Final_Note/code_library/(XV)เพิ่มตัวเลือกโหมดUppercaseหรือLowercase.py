def secret_password(text, key, mode="normal"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            if mode == "uppercase":
                shifted_char = shifted_char.upper()
            elif mode == "lowercase":
                shifted_char = shifted_char.lower()
            result += shifted_char
        else:
            raise ValueError("Error!!!! Input non-characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))
    mode = input("Choose mode (normal/uppercase/lowercase): ").strip().lower()

    ciphertext = secret_password(plaintext, key, mode)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, -key, mode)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

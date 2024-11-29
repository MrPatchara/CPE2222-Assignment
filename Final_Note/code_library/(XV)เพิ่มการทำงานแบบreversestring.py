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
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = secret_password(plaintext, key)
    reversed_ciphertext = ciphertext[::-1]  # Reverse the string
    print("The encrypted ciphertext (reversed):", reversed_ciphertext)

    reversed_decryption = reversed_ciphertext[::-1]
    decrypted_text = secret_password(reversed_decryption, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

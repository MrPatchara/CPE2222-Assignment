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

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")

    # เข้ารหัสแบบ Reverse Alphabet
    ciphertext = reverse_alphabet_encrypt(plaintext)
    print("The encrypted ciphertext (Reverse Alphabet):", ciphertext)

    # ถอดรหัสข้อความด้วยฟังก์ชันเดียวกัน
    decrypted_text = reverse_alphabet_encrypt(ciphertext)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

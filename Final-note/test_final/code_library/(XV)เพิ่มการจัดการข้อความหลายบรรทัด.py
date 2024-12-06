# โปรแกรมเข้ารหัสข้อความด้วยวิธี Caesar Cipher
def secret_password(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        elif char.isspace():  # Allow spaces between words
            result += char
        else:
            raise ValueError("Error!!!! Input contains invalid characters.")
    return result

try:
    plaintext = input("Enter plaintext (Multiple lines allowed, Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    ciphertext = '\n'.join(secret_password(line, key) for line in plaintext.split('\n'))
    print("The encrypted ciphertext (multi-line):")
    print(ciphertext)

    decrypted_text = '\n'.join(secret_password(line, -key) for line in ciphertext.split('\n'))
    print("The decryption result (multi-line):")
    print(decrypted_text)
except ValueError as e:
    print(e)

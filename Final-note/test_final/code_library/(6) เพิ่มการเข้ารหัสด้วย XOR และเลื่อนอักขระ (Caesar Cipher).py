# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR และ Caesar Cipher
def adjust_key_length(plaintext, secret_key):
    """ปรับความยาวของ Secret Key ให้เท่ากับ Plaintext"""
    if len(secret_key) > len(plaintext):
        return secret_key[:len(plaintext)]
    else:
        repeat_times = len(plaintext) // len(secret_key) + 1
        return (secret_key * repeat_times)[:len(plaintext)]

def caesar_cipher(text, shift):
    """เข้ารหัสและถอดรหัสด้วย Caesar Cipher"""
    return ''.join(chr((ord(c) + shift) % 256) for c in text)

def encrypt(plaintext, secret_key, shift=3):
    """เข้ารหัสข้อความด้วย XOR และ Caesar Cipher"""
    xor_cipher = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, secret_key))
    return caesar_cipher(xor_cipher, shift)

def decrypt(ciphertext, secret_key, shift=3):
    """ถอดรหัสข้อความด้วย Caesar Cipher และ XOR"""
    shifted_text = caesar_cipher(ciphertext, -shift)
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(shifted_text, secret_key))

# Main Program
print("------------- Encryption and Decryption Program with Caesar Cipher -------------")

plaintext = input("Enter your plaintext: ")
secret_key = input("Enter your secret key: ")
shift = int(input("Enter the Caesar Cipher shift value: "))

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext = encrypt(plaintext, adjusted_key, shift)
print(f"The encrypted ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, adjusted_key, shift)
print(f"The decryption results: {decrypted_text}\n")
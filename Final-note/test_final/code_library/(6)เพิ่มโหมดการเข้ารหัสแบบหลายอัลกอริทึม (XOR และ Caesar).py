# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR และ Caesar Cipher
def adjust_key_length(plaintext, secret_key):
    """ปรับความยาวของ Secret Key ให้เท่ากับ Plaintext"""
    if len(secret_key) > len(plaintext):
        return secret_key[:len(plaintext)]
    else:
        repeat_times = len(plaintext) // len(secret_key) + 1
        return (secret_key * repeat_times)[:len(plaintext)]

def xor_encrypt(plaintext, secret_key):
    """เข้ารหัสข้อความด้วย XOR"""
    return ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, secret_key))

def caesar_cipher_encrypt(text, shift):
    """เข้ารหัสข้อความด้วย Caesar Cipher"""
    return ''.join(chr((ord(c) + shift) % 256) for c in text)

def caesar_cipher_decrypt(text, shift):
    """ถอดรหัสข้อความด้วย Caesar Cipher"""
    return ''.join(chr((ord(c) - shift) % 256) for c in text)

def encrypt(plaintext, secret_key, shift):
    """เข้ารหัสด้วย XOR และ Caesar"""
    xor_cipher = xor_encrypt(plaintext, secret_key)
    return caesar_cipher_encrypt(xor_cipher, shift)

def decrypt(ciphertext, secret_key, shift):
    """ถอดรหัสด้วย Caesar และ XOR"""
    shifted_text = caesar_cipher_decrypt(ciphertext, shift)
    return xor_encrypt(shifted_text, secret_key)

# Main Program
print("------------- Multi-Algorithm Encryption and Decryption Program -------------")

plaintext = input("Enter your plaintext: ")
secret_key = input("Enter your secret key: ")
shift = int(input("Enter Caesar Cipher shift value: "))

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext = encrypt(plaintext, adjusted_key, shift)
print(f"The encrypted ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, adjusted_key, shift)
print(f"The decryption results: {decrypted_text}\n")
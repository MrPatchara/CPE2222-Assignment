# โปรแกรมนี้เป็นโปรแกรมที่ใช้เข้ารหัสและถอดรหัสข้อความด้วย XOR และใช้ Base64 เข้ารหัส ciphertext
import base64

def encode_base64(data):
    """เข้ารหัส Base64"""
    return base64.b64encode(data.encode()).decode()

def decode_base64(data):
    """ถอดรหัส Base64"""
    return base64.b64decode(data.encode()).decode()

def adjust_key_length(plaintext, secret_key):
    """ปรับความยาวของ Secret Key ให้เท่ากับ Plaintext"""
    if len(secret_key) > len(plaintext):
        return secret_key[:len(plaintext)]
    else:
        repeat_times = len(plaintext) // len(secret_key) + 1
        return (secret_key * repeat_times)[:len(plaintext)]

def encrypt(plaintext, secret_key):
    """เข้ารหัสข้อความด้วย XOR"""
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, secret_key))
    return ciphertext

def decrypt(ciphertext, secret_key):
    """ถอดรหัสข้อความด้วย XOR"""
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, secret_key))
    return plaintext

# Main Program
print("------------- Encryption and Decryption Program -------------")

plaintext = input("Enter your plaintext: ")
secret_key = input("Enter your secret key: ")

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext = encrypt(plaintext, adjusted_key)

encoded_ciphertext = encode_base64(ciphertext)  # เข้ารหัส Base64
print(f"Ciphertext (Base64): {encoded_ciphertext}")

decoded_ciphertext = decode_base64(encoded_ciphertext)  # ถอดรหัส Base64
decrypted_text = decrypt(decoded_ciphertext, adjusted_key)
print(f"The decryption results: {decrypted_text}\n")
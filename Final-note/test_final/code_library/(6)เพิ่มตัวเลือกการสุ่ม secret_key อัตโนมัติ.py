# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR โดยใช้ secret key ที่สร้างขึ้นเองหรือใช้ secret key ที่ผู้ใช้ป้อนเอง
import random
import string

def generate_random_key(length):
    """สร้าง Secret Key แบบสุ่ม"""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

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

random_key_option = input("Do you want to generate a random secret key? (yes/no): ").strip().lower()
if random_key_option == "yes":
    secret_key = generate_random_key(len(plaintext))
    print(f"Generated secret key: {secret_key}")
else:
    secret_key = input("Enter your secret key: ")

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext = encrypt(plaintext, adjusted_key)
print(f"The encrypted ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, adjusted_key)
print(f"The decryption results: {decrypted_text}\n")
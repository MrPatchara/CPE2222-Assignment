# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วยวิธี XOR พร้อมลายนิ้วมือดิจิทัล (Digital Fingerprint)
import hashlib

def generate_fingerprint(data):
    """สร้างลายนิ้วมือดิจิทัล (Digital Fingerprint)"""
    return hashlib.md5(data.encode()).hexdigest()

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
    fingerprint = generate_fingerprint(ciphertext)  # สร้างลายนิ้วมือ
    return ciphertext, fingerprint

def decrypt(ciphertext, secret_key, original_fingerprint):
    """ถอดรหัสข้อความและตรวจสอบลายนิ้วมือ"""
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, secret_key))
    fingerprint = generate_fingerprint(ciphertext)
    if fingerprint != original_fingerprint:
        return plaintext, "Warning: Data might have been altered!"
    return plaintext, "Data integrity verified."

# Main Program
print("------------- Encryption and Decryption Program with Digital Fingerprint -------------")

plaintext = input("Enter your plaintext: ")
secret_key = input("Enter your secret key: ")

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext, fingerprint = encrypt(plaintext, adjusted_key)
print(f"The encrypted ciphertext: {ciphertext}")
print(f"Digital Fingerprint: {fingerprint}")

decrypted_text, verification_message = decrypt(ciphertext, adjusted_key, fingerprint)
print(f"The decryption results: {decrypted_text}")
print(f"Verification: {verification_message}\n")
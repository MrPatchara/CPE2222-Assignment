# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR พร้อมตรวจสอบความถูกต้องด้วย Checksum
import hashlib

def calculate_checksum(data):
    """คำนวณ Checksum ของข้อความ"""
    return hashlib.sha256(data.encode()).hexdigest()

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
    checksum = calculate_checksum(ciphertext)  # คำนวณ Checksum
    return ciphertext, checksum

def decrypt(ciphertext, secret_key, original_checksum):
    """ถอดรหัสข้อความด้วย XOR และตรวจสอบ Checksum"""
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, secret_key))
    checksum = calculate_checksum(ciphertext)  # ตรวจสอบ Checksum
    if checksum != original_checksum:
        return plaintext, "Warning: The ciphertext might have been tampered!"
    return plaintext, "Checksum matched. Data integrity verified."

# Main Program
print("------------- Encryption and Decryption Program with Checksum -------------")

plaintext = input("Enter your plaintext: ")
secret_key = input("Enter your secret key: ")

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext, checksum = encrypt(plaintext, adjusted_key)
print(f"The encrypted ciphertext: {ciphertext}")
print(f"Checksum: {checksum}")

decrypted_text, verification_message = decrypt(ciphertext, adjusted_key, checksum)
print(f"The decryption results: {decrypted_text}")
print(f"Verification: {verification_message}\n")
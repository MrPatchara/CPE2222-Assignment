# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR โดยใช้ secret key ที่กำหนดเอง
def check_key_strength(secret_key):
    """ตรวจสอบความปลอดภัยของ Secret Key"""
    if len(secret_key) < 8:
        return "Weak: The key is too short. Use at least 8 characters."
    if secret_key.isalpha() or secret_key.isdigit():
        return "Weak: The key should contain a mix of letters, digits, and symbols."
    return "Strong: The key is secure."

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
print(f"[The length of plaintext is {len(plaintext)} characters]")

secret_key = input("Enter your secret key: ")
print(f"[The length of secret key is {len(secret_key)} characters]")

key_strength = check_key_strength(secret_key) # ตรวจสอบความแข็งแรงของ Secret Key
print(f"Key Strength: {key_strength}")

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext = encrypt(plaintext, adjusted_key)
print(f"The encrypted ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, adjusted_key)
print(f"The decryption results: {decrypted_text}\n")
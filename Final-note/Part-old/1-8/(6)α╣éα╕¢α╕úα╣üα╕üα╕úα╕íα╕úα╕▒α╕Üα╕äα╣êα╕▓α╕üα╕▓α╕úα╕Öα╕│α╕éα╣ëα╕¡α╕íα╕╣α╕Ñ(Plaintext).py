def adjust_key_length(plaintext, secret_key):
    """ปรับความยาวของ Secret Key ให้เท่ากับ Plaintext"""
    if len(secret_key) > len(plaintext):
        return secret_key[:len(plaintext)]
    else:
        # ทำซ้ำ Secret Key จนกว่าจะมีความยาวเท่ากับ Plaintext
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

# Adjust secret key length
adjusted_key = adjust_key_length(plaintext, secret_key)

# Encrypt the plaintext
ciphertext = encrypt(plaintext, adjusted_key)
print(f"The encrypted ciphertext: {ciphertext}")
print(f"[The length of ciphertext is {len(ciphertext)} characters]")

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, adjusted_key)
print(f"The decryption results: {decrypted_text}\n")
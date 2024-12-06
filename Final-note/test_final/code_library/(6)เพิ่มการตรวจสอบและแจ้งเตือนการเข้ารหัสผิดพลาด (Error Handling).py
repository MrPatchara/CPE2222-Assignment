# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR พร้อมจัดการข้อผิดพลาด
def adjust_key_length(plaintext, secret_key):
    """ปรับความยาวของ Secret Key ให้เท่ากับ Plaintext"""
    if len(secret_key) > len(plaintext):
        return secret_key[:len(plaintext)]
    else:
        repeat_times = len(plaintext) // len(secret_key) + 1
        return (secret_key * repeat_times)[:len(plaintext)]

def encrypt(plaintext, secret_key):
    """เข้ารหัสข้อความด้วย XOR"""
    try:
        ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, secret_key))
        return ciphertext
    except Exception as e:
        return f"Error during encryption: {e}"

def decrypt(ciphertext, secret_key):
    """ถอดรหัสข้อความด้วย XOR"""
    try:
        plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, secret_key))
        return plaintext
    except Exception as e:
        return f"Error during decryption: {e}"

# Main Program
print("------------- Encryption and Decryption Program with Error Handling -------------")

try:
    plaintext = input("Enter your plaintext: ")
    secret_key = input("Enter your secret key: ")

    adjusted_key = adjust_key_length(plaintext, secret_key)
    ciphertext = encrypt(plaintext, adjusted_key)
    if "Error" in ciphertext:
        print(ciphertext)
    else:
        print(f"The encrypted ciphertext: {ciphertext}")

    decrypted_text = decrypt(ciphertext, adjusted_key)
    if "Error" in decrypted_text:
        print(decrypted_text)
    else:
        print(f"The decryption results: {decrypted_text}\n")

except Exception as e:
    print(f"Unexpected error: {e}")
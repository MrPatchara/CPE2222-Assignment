# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR หลายชั้น
def adjust_key_length(plaintext, secret_key):
    """ปรับความยาวของ Secret Key ให้เท่ากับ Plaintext"""
    if len(secret_key) > len(plaintext):
        return secret_key[:len(plaintext)]
    else:
        repeat_times = len(plaintext) // len(secret_key) + 1
        return (secret_key * repeat_times)[:len(plaintext)]

def encrypt(plaintext, secret_key, layers=2):
    """เข้ารหัสข้อความด้วย XOR หลายชั้น"""
    ciphertext = plaintext
    for _ in range(layers):
        ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(ciphertext, secret_key))
    return ciphertext

def decrypt(ciphertext, secret_key, layers=2):
    """ถอดรหัสข้อความด้วย XOR หลายชั้น"""
    plaintext = ciphertext
    for _ in range(layers):
        plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(plaintext, secret_key))
    return plaintext

# Main Program
print("------------- Multi-layer Encryption and Decryption Program -------------")

plaintext = input("Enter your plaintext: ")
secret_key = input("Enter your secret key: ")
layers = int(input("Enter the number of encryption layers: "))

adjusted_key = adjust_key_length(plaintext, secret_key)
ciphertext = encrypt(plaintext, adjusted_key, layers)
print(f"The encrypted ciphertext after {layers} layers: {ciphertext}")

decrypted_text = decrypt(ciphertext, adjusted_key, layers)
print(f"The decryption results: {decrypted_text}\n")
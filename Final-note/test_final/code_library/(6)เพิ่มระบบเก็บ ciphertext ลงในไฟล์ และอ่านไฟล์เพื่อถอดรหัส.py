# โปรแกรมเข้ารหัสและถอดรหัสข้อความด้วย XOR
def save_to_file(filename, content):
    """บันทึกข้อความลงในไฟล์"""
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    """อ่านข้อความจากไฟล์"""
    with open(filename, "r") as file:
        return file.read()

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

filename = "ciphertext.txt"
save_to_file(filename, ciphertext)  # บันทึก Ciphertext ลงไฟล์
print(f"Encrypted ciphertext saved to {filename}.")

ciphertext_from_file = read_from_file(filename)  # อ่าน Ciphertext จากไฟล์
decrypted_text = decrypt(ciphertext_from_file, adjusted_key)
print(f"The decryption results: {decrypted_text}\n")
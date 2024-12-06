# โปรแกรมเข้ารหัสข้อความด้วย key หลายตัว
# โดยใช้ฟังก์ชัน secret_password(text, keys) ที่รับข้อความและ key เป็นอาร์กิวเมนต์
def secret_password(text, keys):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            key = keys[i % len(keys)]  # เลือก key ตามตำแหน่ง
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        else:
            raise ValueError("Error!!!! Input non-characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key_list = list(map(int, input("Enter secret keys (Comma-separated): ").split(',')))

    ciphertext = secret_password(plaintext, key_list)
    print("The encrypted ciphertext:", ciphertext)

    decrypted_text = secret_password(ciphertext, [-key for key in key_list])
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

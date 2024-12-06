# โปรแกรมเข้ารหัสและถอดรหัสข้อความแบบ Transposition Cipher
def transposition_encrypt(text):
    result = ""
    for i in range(0, len(text), 2):
        # สลับตำแหน่งตัวอักษรเป็นคู่ (เช่น AB -> BA)
        if i + 1 < len(text):
            result += text[i + 1] + text[i]
        else:
            result += text[i]  # ตัวสุดท้ายหากเป็นคี่ไม่สลับ
    return result

def transposition_decrypt(text):
    return transposition_encrypt(text)  # สลับกลับใช้ฟังก์ชันเดิม

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")

    # เข้ารหัสแบบ Transposition
    ciphertext = transposition_encrypt(plaintext)
    print("The encrypted ciphertext (Transposition):", ciphertext)

    # ถอดรหัสข้อความ
    decrypted_text = transposition_decrypt(ciphertext)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)

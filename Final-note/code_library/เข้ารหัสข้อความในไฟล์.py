#โปรแกรมเข้ารหัสและถอดรหัสข้อความในไฟล์โดยใช้ Caesar Cipher
def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
        encrypted_content = caesar_cipher(content, shift)
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(encrypted_content)
        print(f"ข้อความถูกเข้ารหัสและบันทึกใน {output_file}")
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {input_file}")

def decrypt_file(input_file, output_file, shift):
    encrypt_file(input_file, output_file, -shift)

# ตัวอย่างการใช้งาน
encrypt_file('plaintext.txt', 'encrypted.txt', 3)
decrypt_file('encrypted.txt', 'decrypted.txt', 3)
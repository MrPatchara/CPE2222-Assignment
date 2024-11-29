#โปรแกรมสร้างรหัสผ่านที่ปลอดภัยและมีความยาวตามที่กำหนด
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# ตัวอย่างการใช้งาน
length = int(input("กรุณาใส่ความยาวของรหัสผ่าน: "))
password = generate_password(length)
print(f"รหัสผ่านที่สร้างคือ: {password}")
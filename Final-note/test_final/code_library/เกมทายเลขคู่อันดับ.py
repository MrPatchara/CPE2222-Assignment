# โปรแกรมทายตัวเลข
# เกมให้ผู้เล่นทายตัวเลขตั้งแต่ 1 ถึง 100 โดยระบบจะบอกว่าคู่หรือคี่และให้คำใบ้"
import random

# สุ่มตัวเลขเป้าหมาย
number = random.randint(1, 100)
attempts = 0

# เริ่มเกม
print("เกมทายตัวเลข (1-100): ระบบจะบอกว่าคู่หรือคี่และให้คำใบ้")
while True:
    guess = int(input("ทายตัวเลขของคุณ: "))
    attempts += 1
    if guess < number:
        print("ตัวเลขต่ำเกินไป! และเป็น", "คู่" if guess % 2 == 0 else "คี่")
    elif guess > number:
        print("ตัวเลขสูงเกินไป! และเป็น", "คู่" if guess % 2 == 0 else "คี่")
    else:
        print(f"คุณทายถูกต้อง! ตัวเลขคือ {number} ใช้เวลา {attempts} ครั้ง")
        break

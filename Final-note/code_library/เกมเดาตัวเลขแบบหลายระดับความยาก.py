#เกมให้ผู้เล่นเดาตัวเลขโดยเลือกระดับความยากที่ส่งผลต่อช่วงตัวเลขและจำนวนครั้งในการทาย"
import random

def number_guessing_game(level):
    if level == 'ง่าย':
        range_start, range_end, attempts = 1, 10, 5
    elif level == 'ปานกลาง':
        range_start, range_end, attempts = 1, 50, 7
    elif level == 'ยาก':
        range_start, range_end, attempts = 1, 100, 10
    else:
        print("เลือกระดับความยากไม่ถูกต้อง")
        return

    target_number = random.randint(range_start, range_end)
    print(f"เริ่มเกม! ตัวเลขอยู่ในช่วง {range_start} ถึง {range_end} คุณมีโอกาส {attempts} ครั้ง")

    for _ in range(attempts):
        guess = int(input("ทายตัวเลขของคุณ: "))
        if guess == target_number:
            print(f"ยินดีด้วย! คุณทายถูกต้อง ตัวเลขคือ {target_number}")
            return
        elif guess < target_number:
            print("ตัวเลขต่ำเกินไป!")
        else:
            print("ตัวเลขสูงเกินไป!")
    
    print(f"เสียใจด้วย! คุณใช้โอกาสหมดแล้ว ตัวเลขคือ {target_number}")

# ตัวอย่างการใช้งาน
level = input("เลือกระดับความยาก (ง่าย/ปานกลาง/ยาก): ")
number_guessing_game(level)
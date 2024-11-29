#เกมให้ผู้เล่นจัดเรียงตัวเลขที่แสดงแบบสุ่ม
import random

def play_number_sequence_game(size):
    sequence = list(range(1, size + 1))
    shuffled_sequence = sequence[:]
    random.shuffle(shuffled_sequence)

    print("ลำดับตัวเลขสุ่ม:")
    print(shuffled_sequence)
    print("ให้จัดเรียงตัวเลขให้ถูกต้อง")

    user_sequence = list(map(int, input("ใส่ลำดับตัวเลขที่เรียง (คั่นด้วยช่องว่าง): ").split()))
    if user_sequence == sequence:
        print("ยินดีด้วย! คุณจัดเรียงถูกต้อง")
    else:
        print(f"ผิด! ลำดับที่ถูกต้องคือ {sequence}")

# ตัวอย่างการใช้งาน
play_number_sequence_game(5)
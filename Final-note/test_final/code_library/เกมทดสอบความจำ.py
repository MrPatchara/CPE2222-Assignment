# โปรแกรมทดสอบความจำ
#เกมให้ผู้เล่นจดจำและเรียงลำดับตัวเลขที่แสดงในเวลาจำกัด
import random
import time

def memory_test_game():
    print("เกมทดสอบความจำ!")
    sequence = [random.randint(1, 9) for _ in range(5)]
    print("ตัวเลขที่จะต้องจำ:")
    print(sequence)
    time.sleep(3)
    print("\033[H\033[J")  # เคลียร์หน้าจอ
    user_input = input("ใส่ตัวเลขที่คุณจำได้ (คั่นด้วยช่องว่าง): ")
    user_sequence = list(map(int, user_input.split()))
    if user_sequence == sequence:
        print("ยินดีด้วย! คุณจำได้ถูกต้อง")
    else:
        print(f"ผิด! ลำดับที่ถูกต้องคือ {sequence}")

# ตัวอย่างการใช้งาน
memory_test_game()
user_input = input("กรุณาป้อนตัวเลข: ")

try:
    result = int(user_input) + "Hello"  # การบวกตัวเลขกับข้อความทำให้เกิด TypeError
except TypeError as e:
    print("เกิดข้อผิดพลาดประเภทข้อมูล:", e)
    print("ไม่สามารถดำเนินการบวกระหว่างประเภทข้อมูลที่ต่างกันได้")
else:
    print("ผลลัพธ์การคำนวณ:", result)


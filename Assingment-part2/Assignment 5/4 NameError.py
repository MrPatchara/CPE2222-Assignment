try:
    # รับชื่อของตัวแปรจากผู้ใช้
    name = input("กรุณากรอกชื่อตัวแปรที่ต้องการพิมพ์ค่า: ")
    
    # ใช้ eval เพื่อพยายามเข้าถึงตัวแปรที่ผู้ใช้ใส่
    print(eval(name))  # ถ้าตัวแปรไม่มีอยู่ จะเกิด NameError
except NameError as e:
    print("เกิดข้อผิดพลาด NameError:", e)
    print("ตัวแปรที่คุณระบุยังไม่ได้กำหนด")
else:
    print("สามารถเข้าถึงตัวแปรได้สำเร็จ")



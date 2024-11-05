try:
    # รับชื่อไฟล์จากผู้ใช้
    filename = input("กรุณากรอกชื่อไฟล์ที่ต้องการเปิด: ")
    
    # พยายามเปิดไฟล์ตามชื่อที่ผู้ใช้ระบุ
    with open(filename, 'r') as file:
        content = file.read()
        print("เนื้อหาในไฟล์:", content)
except FileNotFoundError as e:
    print("เกิดข้อผิดพลาด FileNotFoundError:", e)
    print("ไม่พบไฟล์ที่ระบุ")
else:
    print("เปิดไฟล์สำเร็จและอ่านเนื้อหาได้โดยไม่มีข้อผิดพลาด")



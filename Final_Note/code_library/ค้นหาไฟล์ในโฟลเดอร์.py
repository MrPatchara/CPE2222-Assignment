#โปรแกรมค้นหาไฟล์ที่มีคำสำคัญในชื่อไฟล์ภายในโฟลเดอร์
import os

def search_files(folder, keyword):
    matched_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if keyword in file:
                matched_files.append(os.path.join(root, file))
    return matched_files

# ตัวอย่างการใช้งาน
folder = input("กรุณาใส่ชื่อโฟลเดอร์ที่ต้องการค้นหา: ")
keyword = input("ใส่คำสำคัญในชื่อไฟล์ที่ต้องการค้นหา: ")
results = search_files(folder, keyword)
if results:
    print("พบไฟล์ที่ตรงกับคำค้นหา:")
    for file in results:
        print(file)
else:
    print("ไม่พบไฟล์ที่ตรงกับคำค้นหา")
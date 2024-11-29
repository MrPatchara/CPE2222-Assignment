import os
import shutil

def batch_copy_files(source_folder, destination_folder):
    # ตรวจสอบว่าโฟลเดอร์ต้นทางมีอยู่
    if not os.path.exists(source_folder):
        print(f"ไม่พบโฟลเดอร์ต้นทาง: {source_folder}")
        return

    # สร้างโฟลเดอร์ปลายทางถ้าไม่มี
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # คัดลอกไฟล์ทั้งหมด
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"คัดลอก {filename} ไปยัง {destination_folder}")

# ตัวอย่างการใช้งาน
source = "source_folder"  # เปลี่ยนชื่อโฟลเดอร์ต้นทาง
destination = "destination_folder"  # เปลี่ยนชื่อโฟลเดอร์ปลายทาง
batch_copy_files(source, destination)
